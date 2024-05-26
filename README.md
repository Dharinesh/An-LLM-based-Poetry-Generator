# Sample Output:

![image](https://github.com/Dharinesh/An-LLM-based-Poetry-Generator/assets/108059896/cc32655a-3337-4ee6-aecd-ccadd9a5d363)

# Poetry Generator

This is a simple Streamlit app that generates poetry based on user-provided mood, theme, and style preferences. The app utilizes the LLama-2 language model from Anthropic to generate the poems.

## Prerequisites

Before running the app, make sure you have the following dependencies installed:

- Python (version 3.6 or later)
- Streamlit
- LangChain
- LangChain Community LLMs (for CTransformers)

You can install the required Python packages using pip:

```pip install streamlit langchain langchain-community-llms```

## Usage

1. Clone or download the repository to your local machine.
   use the command:
    ``` pip install -r requirements.txt```
   
3. Navigate to the project directory.
4. Run the Streamlit app using the following command:

    ```streamlit run app.py```

5. The app will open in your default web browser. If it doesn't open automatically, you can access it by clicking the URL provided in the terminal.
6. In the app interface, enter the desired mood, theme, and style for the poem you want to generate.
7. Click the "Generate Poem" button.
8. The generated poem will be displayed in the app, with line breaks preserved.

Note: Make sure to have the model downloaded, and save it in the models folder in the project directory.
You can download the model from Hugging Face:  [Hugging Face]([https://example.com](https://huggingface.co/)) 
    -offcial meta models requiries signing up tp terms and conditions
    
## Code Overview

The code consists of the following components:

- `getPoetry` function: This function takes the mood, theme, and style as input and uses the LLama-2 model to generate a poem. It also includes a prompt template to guide the model in generating the desired output.
- Streamlit app: The main part of the code sets up the Streamlit app user interface, including text input fields for mood, theme, and style, and a button to generate the poem. When the button is clicked, the `getPoetry` function is called with the user inputs, and the generated poem is displayed using the `st.code` function, which preserves line breaks.

## Customization

You can customize the app by modifying the following aspects:

- Prompt template: Modify the `template` string in the `getPoetry` function to change the instructions provided to the language model.
- Language model: Change the `model` parameter in the `CTransformers` initialization to use a different language model.
- Model configuration: Adjust the `config` parameter in the `CTransformers` initialization to modify the model's behavior, such as changing the temperature or the maximum number of generated tokens.
- Streamlit app UI: Modify the Streamlit app code to change the user interface, add additional features, or customize the styling.

## License

This project is licensed under the [GNU GENERAL PUBLIC LICENSE](LICENSE).
