import boto3
import json
from difflib import get_close_matches
from typing import Union
import wikipediaapi
from nltk.tokenize import sent_tokenize

# AWS kimlik bilgileri
aws_access_key_id = 'acces_key'
aws_secret_access_key = 'secret_acces_key'
region_name = 'region_here'

# S3 bağlantısı
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                  region_name=region_name)


def read_json_from_s3():
    bucket_name = 'chatbotdataset'
    json_file_key = 'knowledge_base.json'

    try:
        response = s3.get_object(Bucket=bucket_name, Key=json_file_key)
        json_data = json.loads(response['Body'].read().decode('utf-8'))
        return json_data
    except Exception as e:
        print(f"Hata: {str(e)}")
        return None


def write_json_to_s3(data):
    bucket_name = 'chatbotdataset'
    json_file_key = 'knowledge_base.json'

    try:
        s3.put_object(Bucket=bucket_name, Key=json_file_key, Body=json.dumps(data, indent=2))
    except Exception as e:
        print(f"Hata: {str(e)}")


def find_best_match(user_question: str, questions: list[str]) -> Union[str, None]:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.81)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict) -> Union[str, None]:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None


user_agent = "My-Chatbot/1.0 (email_adress)"


wiki_wiki = wikipediaapi.Wikipedia('My-Chatbot/1.0 (email_adress)', 'en')


def search_wikipedia(user_input):
    if user_input.lower().endswith(" vikipedi"):
        search_term = user_input[:-8].strip()
        result = wiki_wiki.page(search_term)
        if result.exists():
            text = result.text
            max_chars = 450  # Toplam karakter sınırı
            max_chars_per_line = 100  # Satır başına maksimum karakter sayısı

            sentences = sent_tokenize(text)
            lines = []
            line = ""
            for sentence in sentences:
                words = sentence.split()
                for word in words:
                    if len(line) + len(word) <= max_chars_per_line:
                        if line:
                            line += " " + word
                        else:
                            line = word
                    else:
                        lines.append(line)
                        line = word

                        if len(line) > max_chars_per_line:
                            # Handle the case where a single word exceeds the character limit
                            # Split the word into chunks of max_chars_per_line
                            chunks = [line[i:i + max_chars_per_line] for i in range(0, len(line), max_chars_per_line)]
                            lines.extend(chunks[:-1])  # Append all except the last chunk
                            line = chunks[-1]  # Last chunk becomes the new line

                if line:
                    lines.append(line)
                    line = ""

            final_text = ""
            total_chars = 0
            for line in lines:
                if total_chars + len(line) <= max_chars:
                    if len(final_text + line) <= max_chars:
                        final_text += line + "\n"
                        total_chars += len(line)
                    else:
                        break
                else:
                    break

            return final_text.strip()
        else:
            return "Aradığınız terim Vikipedi'de bulunamadı."
    else:
        return None


def interact_with_s3():
    json_data = read_json_from_s3()
    if json_data is None:
        json_data = {"questions": []}

    while True:
        user_input = input('You: ')

        if user_input.lower() == 'quit':
            break

        if user_input.lower().endswith("vikipedi"):
            wikipedia_result = search_wikipedia(user_input)
            print('Bot:', wikipedia_result)
        else:
            best_match = find_best_match(user_input, [q["question"] for q in json_data["questions"]])

            if best_match is not None:
                answer = get_answer_for_question(best_match, json_data)
                print(f'Bot: {answer}')
            else:
                print('Bot: I don\'t know the answer. Can you teach me?')
                new_answer = input('Type the answer or "skip" to skip: ')

                if new_answer.lower() != 'skip':
                    json_data["questions"].append({"question": user_input, "answer": new_answer})
                    write_json_to_s3(json_data)
                    print('Bot: Thank you! I learned a new response!')
