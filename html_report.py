from html_writer import Html


class HtmlReport:
    def __init__(self):
        self.body = Html()

    def add_section(self, title: str = "", summary: str = "", top_terms: list = None):
        top_terms = [] if top_terms is None else top_terms

        with self.body.tag('div'):
            self.body.tag_with_content(title, name='h1')
            self.body.tag_with_content(summary, name='p')
            self.body.tag_with_content(f"Top terms: {', '.join(top_terms)}", name="p")

    def to_html(self):
        return Html.html_template(Html(), self.body).to_raw_html(2)