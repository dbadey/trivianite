#disney

from openai import OpenAI
import json
import os

# Configure with API key
    # client = OpenAI(api_key="my-key")

#read key from environment variable automatically
    #on mac terminal: export OPENAI_API_KEY="my-key"
    #to create permanent environemnt variable: open ~/.zshrc, export OPENAI_API_KEY="my-key" and save, source ~/.zshrc, echo $OPENAI_API_KEY
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": (
                "My theme is Disney. Create 4 trivia categories and 10 questions per category"
                "Questions should NOT be multiple choice. "
                "Return ONLY valid JSON in this format:\n\n"
                "{\n"
                "  \"categories\": [\n"
                "    {\n"
                "      \"category_name\": \"string\",\n"
                "      \"questions\": [\n"
                "        {\n"
                "          \"question\": \"string\",\n"
                "          \"correct_answer\": \"string\"\n"
                "        }\n"
                "      ]\n"
                "    }\n"
                "  ]\n"
                "}"
            )
        }
    ],
    response_format={"type": "json_object"}  # forces valid JSON
)

# Convert response to Python dictionary automatically
trivia_data = json.loads(response.choices[0].message.content)
print(trivia_data)


"""
{
  "categories": [
    {
      "category_name": "Disney Princesses",
      "questions": [
        {
          "question": "What is the name of Ariel’s father in The Little Mermaid?",
          "correct_answer": "King Triton"
        },
        {
          "question": "What kingdom does Elsa rule in Frozen?",
          "correct_answer": "Arendelle"
        },
        {
          "question": "What is the name of Belle’s father in Beauty and the Beast?",
          "correct_answer": "Maurice"
        },
        {
          "question": "What is the name of Cinderella’s magical carriage item before transformation?",
          "correct_answer": "Pumpkin"
        },
        {
          "question": "Which warrior princess is the daughter of Chief Powhatan?",
          "correct_answer": "Pocahontas"
        },
        {
          "question": "What is the name of Mulan’s dragon companion?",
          "correct_answer": "Mushu"
        },
        {
          "question": "What is Snow White’s signature fruit?",
          "correct_answer": "Apple"
        },
        {
          "question": "What is the name of Jasmine’s pet tiger in Aladdin?",
          "correct_answer": "Rajah"
        },
        {
          "question": "What is the name of Merida’s kingdom in Brave?",
          "correct_answer": "DunBroch"
        },
        {
          "question": "What is the name of Rapunzel’s love interest in Tangled?",
          "correct_answer": "Flynn Rider"
        }
      ]
    },
    {
      "category_name": "Disney Villains",
      "questions": [
        {
          "question": "Who is the main villain in The Lion King?",
          "correct_answer": "Scar"
        },
        {
          "question": "What is the name of the sea witch in The Little Mermaid?",
          "correct_answer": "Ursula"
        },
        {
          "question": "Who is the evil fairy in Sleeping Beauty?",
          "correct_answer": "Maleficent"
        },
        {
          "question": "Who is the power-hungry vizier in Aladdin?",
          "correct_answer": "Jafar"
        },
        {
          "question": "What is Cruella’s last name in 101 Dalmatians?",
          "correct_answer": "De Vil"
        },
        {
          "question": "Who kidnaps Penny in The Rescuers?",
          "correct_answer": "Madame Medusa"
        },
        {
          "question": "Who rules the Underworld in Hercules?",
          "correct_answer": "Hades"
        },
        {
          "question": "Who is the villain obsessed with youth in Tangled?",
          "correct_answer": "Mother Gothel"
        },
        {
          "question": "Who is the villainous prince in Frozen?",
          "correct_answer": "Prince Hans"
        },
        {
          "question": "Who is the hunter sent to kill Snow White?",
          "correct_answer": "The Huntsman"
        }
      ]
    },
    {
      "category_name": "Pixar Films",
      "questions": [
        {
          "question": "What type of fish is Nemo in Finding Nemo?",
          "correct_answer": "Clownfish"
        },
        {
          "question": "What is the name of the cowboy doll in Toy Story?",
          "correct_answer": "Woody"
        },
        {
          "question": "What is the name of the elderly man in Up?",
          "correct_answer": "Carl Fredricksen"
        },
        {
          "question": "What kind of vehicle is Lightning McQueen in Cars?",
          "correct_answer": "Race car"
        },
        {
          "question": "What is the name of the robot left on Earth in WALL-E?",
          "correct_answer": "WALL-E"
        },
        {
          "question": "What family power does Elastigirl have in The Incredibles?",
          "correct_answer": "Elasticity"
        },
        {
          "question": "What is the name of Miguel’s dog in Coco?",
          "correct_answer": "Dante"
        },
        {
          "question": "What is the name of the blue monster in Monsters, Inc.?",
          "correct_answer": "James P. Sullivan"
        },
        {
          "question": "Where do the emotions live in Inside Out?",
          "correct_answer": "Riley’s mind"
        },
        {
          "question": "What sport does Luca compete in while in human form?",
          "correct_answer": "Triathlon"
        }
      ]
    },
    {
      "category_name": "Classic Disney Movies",
      "questions": [
        {
          "question": "What is the name of the wooden puppet who wants to become a real boy?",
          "correct_answer": "Pinocchio"
        },
        {
          "question": "What magical creature grants wishes in Aladdin?",
          "correct_answer": "Genie"
        },
        {
          "question": "What is the name of Bambi’s rabbit friend?",
          "correct_answer": "Thumper"
        },
        {
          "question": "What is the name of the boy who never grows up in Peter Pan?",
          "correct_answer": "Peter Pan"
        },
        {
          "question": "What is the name of the fairy in Peter Pan?",
          "correct_answer": "Tinker Bell"
        },
        {
          "question": "What is the name of the elephant who can fly in Dumbo?",
          "correct_answer": "Dumbo"
        },
        {
          "question": "What is the name of the jungle boy raised by wolves in The Jungle Book?",
          "correct_answer": "Mowgli"
        },
        {
          "question": "What is the name of the dog in Lady and the Tramp?",
          "correct_answer": "Lady"
        },
        {
          "question": "Who is the villain in 101 Dalmatians?",
          "correct_answer": "Cruella De Vil"
        },
        {
          "question": "What is the name of the deer in Bambi?",
          "correct_answer": "Bambi"
        }
      ]
    }
  ]
}
"""