import argparse

from entity_counter import EntityCounter
from html_report import HtmlReport
from papers import HuggingFacePapers
from summarizer import Summarizer


# Fixed constants for now, can be cmd line args in the future
NUM_SENTENCES_SUMMARY = 5
NUM_ENTITIES = 5


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--token", help="HuggingFace Serverless Inference token", required=True)
parser.add_argument("-y", "--year", help="Year(s) to retrieve HuggingFace Papers, eg. 2025,2024",
                    default="2025", type=lambda s: s.split(','))
parser.add_argument("-m", "--month", help="Month(s) to retrieve HuggingFace Papers, eg. 01,02,03",
                    default="01", type=lambda s: s.split(','))
parser.add_argument("-k", "--top_k", help="How many documents to retrieve per month", default=5)
parser.add_argument("-o", "--output", help="Output filename", default="report.html")

args = parser.parse_args()

summarizer = Summarizer(args.token)
entity_counter = EntityCounter()
report = HtmlReport()


for year in args.year:
    for month in args.month:
        print(f'Retrieving and summarizing HuggingFace papers for {month}-{year}')
        papers = HuggingFacePapers.from_year_month(year, month, args.top_k)
        summary = summarizer.summarize(papers, NUM_SENTENCES_SUMMARY)
        entities = [ entity for (entity, _) in entity_counter.top_entities(papers, NUM_ENTITIES) ]
        report.add_section(
            f"HuggingFace Papers for {month}-{year}",
            summary,
            entities
        )

with open(args.output, 'x') as output:
    output.write(report.to_html())

print(f"Report written to {args.output}")