import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

def optimize_listing(raw_description):
    """
    Receives raw text from a seller and generates a structured,
    optimized listing with SEO elements for a global marketplace.
    """
    print("Optimizing listing and generating SEO data...")

    prompt = f"""
    You are an expert in e-commerce, copywriting, and SEO for global equestrian marketplaces.
    Optimize the following seller description for an international audience. 
    
    Generate the following parts:
    1. Optimized Title (Engaging, searchable, max 60 characters).
    2. Structured Description (Cleanly formatted with bullet points for breed, age, training level, or condition).
    3. SEO Meta Description (Max 160 characters).

    Raw seller description:
    {raw_description}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional e-commerce and SEO expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        
        return response.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    sample_listing = """
    Selling a nice 8-year-old gelding, jumps 120 cm courses, super sweet to hack out on 
    and in all handling, selling due to lack of time. Price negotiable for a smooth deal.
    """

    result = optimize_listing(sample_listing)
    print("\n--- OPTIMIZED LISTING & SEO ---")
    print(result)
