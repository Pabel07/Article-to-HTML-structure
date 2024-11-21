from openai import OpenAI
import os


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)



def structure_article_to_html(article_text):
    """
    Takes an article text and structures it as an HTML file using OpenAI's GPT.

    :param article_text: The raw article text to be structured.
    :return: A string containing the structured HTML content.
    """
    prompt = (
        "Take the following article and structure it as a clean, semantic HTML file. "
        "Use proper tags such as <h1>, <h2>, <p>, <ul>, <ol>, etc., where appropriate. "
        "Use <ul> or <ol> tags only if the text contains lists, such as items starting with dashes (-), numbers (e.g., 1., 2., 3.), or similar patterns. "
        "Include basic indentation for readability. "
        "Identify places where it would be beneficial to insert images, based on expertise in writing blog articles and SEO knowledge. "
        "At these locations, add an ***image*** "
        "Also add an ***main_image*** below <h1> tag"
        "Return only the HTML code contained within the <body> tag, excluding the <body> tags themselves.\n\n"
        f"Article:\n{article_text}\n\n"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an assistant skilled in converting articles to HTML format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )
        # Extract the HTML content from the response
        html_content = response.choices[0].message.content


        return html_content

    except Exception as e:
        return f"An error occurred: {e}"

def html_output_with_images(article_text):
    """
    Takes an article text and structures it as an HTML file using OpenAI's GPT.

    :param article_text: Structured HTML content.
    :return: A string containing the structured HTML content with images ideas.
    """
    article_html = structure_article_to_html(article_text)

    prompt = (
        "You are an expert in writing high-quality articles and blogs. "
        "You are given an article in HTML format with placeholders ***image*** and ***main_image***. "
        "For each ***image*** placeholder: "
        "1. Analyze the surrounding text to determine an appropriate image concept that enhances the article's value for readers and aligns with SEO best practices. "
        "2. Replace the placeholder with an <img> tag using src='image_placeholder.jpg'. "
        "3. Add an alt attribute to the <img> tag describing the image content, based on the surrounding text, in a way suitable as a prompt for generating the image. "
        "4. Directly below the <img> tag, insert a short sentence (in the language of article) summarizing the key insight from the surrounding text, wrapped in a <p> tag with class='caption-text', to further engage the reader. "
        "For the ***main_image*** placeholder: "
        "1. Analyze the overall topic and content of the article to determine a suitable image concept that captures the essence of the article. "
        "2. Replace the placeholder with an <img> tag using src='main_image_placeholder.jpg'. "
        "3. Add an alt attribute describing the main image content based on the article's topic, ensuring it is engaging and descriptive. "
        "Ensure the final output is semantic, well-indented HTML and reflects a professional, reader-focused approach. "
        "Return only the updated HTML structure.\n\n"
        f"Article:\n{article_html}\n\n"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an assistant skilled in converting articles to HTML format."},
                {"role": "user", "content": prompt}
            ],
            temperature=1
        )
        # Extract the HTML content from the response
        html_content = response.choices[0].message.content
        html_content = html_content.replace("```html\n", "").replace("```", "")

        return html_content

    except Exception as e:
        return f"An error occurred: {e}"


def read_article_from_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

if __name__ == "__main__":
    file_path = "article.txt"
    article_text = read_article_from_txt(file_path)

    html_output = html_output_with_images(article_text)

    with open('artykul.html', 'w', encoding='utf-8') as file:
        file.write(html_output)

    print("Wygenerowany tekst zapisano do pliku 'artykul.html'.")