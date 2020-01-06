from emailer import Emailer
from csv_handler import generate_csv, get_list_from_csv
import os
import sys


if __name__ == '__main__':

    DEBUG = False

    if DEBUG:
        class Logger:
            @staticmethod
            def info(text):
                print(text)

    emailer = Emailer(os.getenv('EMAILER_ADDRESS'),
                      os.getenv('EMAILER_PASSWORD'))

    input_file = 'sample_in.csv'  # CSV with all therapists email
    output_file = 'sample_out.csv'  # CSV with all the already sent emails

    all_therapists = get_list_from_csv(input_file)
    all_sent_therapists = get_list_from_csv(output_file)
    all_sent_emails = [therapist['contact_email']
                       for therapist in all_sent_therapists]

    NUM_OF_EMAILS_TO_SEND = None
    NUM_OF_EMAILS_SENT_NOW = 0
    if len(sys.argv) > 1:
        try:
            NUM_OF_EMAILS_TO_SEND = int(sys.argv[1])
        except:
            raise TypeError
    else:
        NUM_OF_EMAILS_TO_SEND = len(all_therapists) - len(all_sent_emails)

    print(f'Preparing to send {NUM_OF_EMAILS_TO_SEND} email(s)...\n')
    for therapist in all_therapists:
        if NUM_OF_EMAILS_SENT_NOW >= NUM_OF_EMAILS_TO_SEND:
            break
        if therapist['contact_email'] not in all_sent_emails:
            if emailer.run('CAMPAIGN', therapist, Logger if DEBUG else None):
                print(f"Email sent to {therapist['contact_email']}\n")
                NUM_OF_EMAILS_SENT_NOW += 1
                all_sent_therapists.append(therapist)
            else:
                print(
                    f"ERROR SENDING EMAIL TO: {therapist['full_name']}, {therapist['contact_email']}\n")
    print(f'{NUM_OF_EMAILS_SENT_NOW} email(s) have been sent now\n\n')
    print(
        f'Campaign Status: {len(all_sent_therapists)} of {len(all_therapists)}')
    generate_csv(output_file, all_sent_therapists)
