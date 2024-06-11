import pandas as pd

def annotate_paragraphs(csv_file):
    # Load the CSV file
    df = pd.read_csv(csv_file)
    
    # Find the index of the first row that doesn't have a label
    start_index = df[df['label'].isnull()].index[0]
    
    # Iterate through the paragraphs
    for i in range(start_index, len(df)):
        print('--------------------------------------------------------------------------------')

        print(f'[{i} / {len(df)}]')

        paragraph1 = df.loc[i, 'paragraph1']
        paragraph2 = df.loc[i, 'paragraph2']
        
        print("Paragraph 1:")
        print(paragraph1)
        print("\nParagraph 2:")
        print(paragraph2)
        
        # Get user input for annotation
        label = input("Enter label (1 or 0): ")
        
        # Check if the input is valid
        while label not in ['1', '0']:
            print("Invalid input. Please enter 1 or 0.")
            label = input("Enter label (1 or 0): ")
        
        # Save the label in the DataFrame
        df.loc[i, 'label'] = int(label)
        
        # Save the DataFrame back to the CSV file
        df.to_csv(csv_file, index=False)
        
        # Check if the user wants to continue annotating
        cont = input("Do you want to continue annotating? (y/n): ")

        print('--------------------------------------------------------------------------------')
        if cont.lower() != 'y':
            break


# Example usage
annotate_paragraphs('./data/test_annotation.csv')
