# # data_manager.py V1
# import pandas as pd
# import os
# import json

# # --- Private variables to store the loaded menu in different formats ---
# _menu_df = None
# _menu_as_string = None
# _menu_as_dict = None

# def _initialize_menu():
#     """
#     Internal function to load and process the menu from the correctly structured Excel file.
#     This is called once to populate all menu formats.
#     """
#     global _menu_df, _menu_as_string, _menu_as_dict
    
#     # Prevents reloading if already loaded
#     if _menu_df is not None:
#         return

#     filename = 'namasthe_hounslow_menu.xlsx'
#     file_path = os.path.join(os.path.dirname(__file__), 'data', filename)
    
#     try:
#         if not os.path.exists(file_path):
#             raise FileNotFoundError

#         # Load the Excel file, assuming the first row is the header
#         df = pd.read_excel(file_path)
        
#         # --- FIX FOR KeyError ---
#         # Standardize column names: remove leading/trailing spaces and convert to lowercase.
#         # This makes the code robust against "Item Name" vs "itemname" vs " Item Name ".
#         df.columns = [str(col).strip().lower() for col in df.columns]
        
#         # Rename 'item name' to 'itemname' for consistency if it exists
#         if 'item name' in df.columns:
#             df.rename(columns={'item name': 'itemname'}, inplace=True)

#         # --- Data Validation ---
#         required_columns = ['category', 'itemname', 'price']
#         for col in required_columns:
#             if col not in df.columns:
#                 raise KeyError(f"The required column '{col}' was not found in your Excel file. Please check the spelling and structure.")

#         # Ensure 'price' column is numeric, coercing errors to NaN (Not a Number)
#         df['price'] = pd.to_numeric(df['price'], errors='coerce')
        
#         # Drop rows where essential information is missing
#         df.dropna(subset=['itemname', 'price', 'category'], inplace=True)

#         _menu_df = df
        
#         # Create the JSON string version for the AI
#         _menu_as_string = _menu_df.to_json(orient='records', indent=4)
        
#         # Create the dictionary version for the bot logic, grouped by category
#         _menu_as_dict = _menu_df.groupby('category').apply(lambda x: x.to_dict('records')).to_dict()

#         print(f"✅ Menu loaded and processed successfully from {filename}")
        
#     except FileNotFoundError:
#         print(f"❌ ERROR: Menu file not found. Make sure '{filename}' is in the 'data' folder.")
#     except KeyError as e:
#         print(f"❌ ERROR: {e}")
#     except Exception as e:
#         print(f"❌ An unexpected error occurred while loading the menu: {e}")

# def get_menu_as_string():
#     """Returns the full menu as a JSON formatted string for the AI."""
#     return _menu_as_string

# def get_menu_as_dict():
#     """Returns the menu as a dictionary, grouped by category."""
#     return _menu_as_dict

# def get_item_details(item_name):
#     """Finds a specific item in the menu DataFrame and returns its details."""
#     if _menu_df is None:
#         return None
#     # Case-insensitive search for the item
#     item = _menu_df[_menu_df['itemname'].str.lower() == item_name.lower()]
#     if not item.empty:
#         return item.iloc[0].to_dict()
#     return None

# # --- Initialize the menu when the module is first imported ---
# _initialize_menu()








# # data_manager.py V2
# import pandas as pd
# import os
# import json

# # --- Private variables to store the loaded menu in different formats ---
# _menu_df = None
# _menu_as_string = None
# _menu_as_dict = None

# def _initialize_menu():
#     """
#     Internal function to load and process the menu from the correctly structured Excel file.
#     This is called once to populate all menu formats.
#     """
#     global _menu_df, _menu_as_string, _menu_as_dict
    
#     # Prevents reloading if already loaded
#     if _menu_df is not None:
#         return

#     filename = 'namasthe_hounslow_menu.xlsx'
#     file_path = os.path.join(os.path.dirname(__file__), 'data', filename)
    
#     try:
#         if not os.path.exists(file_path):
#             raise FileNotFoundError

#         # Load the Excel file, assuming the first row is the header
#         df = pd.read_excel(file_path)
        
#         # --- FIX FOR KeyError ---
#         # Standardize column names: remove leading/trailing spaces and convert to lowercase.
#         # This makes the code robust against "Item Name" vs "itemname" vs " Item Name ".
#         df.columns = [str(col).strip().lower() for col in df.columns]
        
#         # Rename 'item name' to 'itemname' for consistency if it exists
#         if 'item name' in df.columns:
#             df.rename(columns={'item name': 'itemname'}, inplace=True)

#         # --- Data Validation ---
#         required_columns = ['category', 'itemname', 'price']
#         for col in required_columns:
#             if col not in df.columns:
#                 raise KeyError(f"The required column '{col}' was not found in your Excel file. Please check the spelling and structure.")

#         # Ensure 'price' column is numeric, coercing errors to NaN (Not a Number)
#         df['price'] = pd.to_numeric(df['price'], errors='coerce')
        
#         # Drop rows where essential information is missing
#         df.dropna(subset=['itemname', 'price', 'category'], inplace=True)

#         _menu_df = df
        
#         # Create the JSON string version for the AI
#         _menu_as_string = _menu_df.to_json(orient='records', indent=4)
        
#         # Create the dictionary version for the bot logic, grouped by category
#         _menu_as_dict = _menu_df.groupby('category').apply(lambda x: x.to_dict('records')).to_dict()

#         print(f"✅ Menu loaded and processed successfully from {filename}")
        
#     except FileNotFoundError:
#         print(f"❌ ERROR: Menu file not found. Make sure '{filename}' is in the 'data' folder.")
#     except KeyError as e:
#         print(f"❌ ERROR: {e}")
#     except Exception as e:
#         print(f"❌ An unexpected error occurred while loading the menu: {e}")

# def get_menu_as_string():
#     """Returns the full menu as a JSON formatted string for the AI."""
#     return _menu_as_string

# def get_menu_as_dict():
#     """Returns the menu as a dictionary, grouped by category."""
#     return _menu_as_dict

# def get_item_details(item_name):
#     """Finds a specific item in the menu DataFrame and returns its details."""
#     if _menu_df is None:
#         return None
#     # Case-insensitive search for the item
#     item = _menu_df[_menu_df['itemname'].str.lower() == item_name.lower()]
#     if not item.empty:
#         return item.iloc[0].to_dict()
#     return None

# # --- Initialize the menu when the module is first imported ---
# _initialize_menu()










# # data_manager.py Confirmed
# import pandas as pd
# import os
# import json

# # --- Private variables to store the loaded menu in different formats ---
# _menu_df = None
# _menu_as_string = None
# _menu_as_dict = None

# def _initialize_menu():
#     """
#     Internal function to load and process the menu from the correctly structured Excel file.
#     """
#     global _menu_df, _menu_as_string, _menu_as_dict
    
#     if _menu_df is not None:
#         return

#     filename = 'namasthe_hounslow_menu.xlsx'
#     file_path = os.path.join(os.path.dirname(__file__), 'data', filename)
    
#     try:
#         if not os.path.exists(file_path):
#             raise FileNotFoundError

#         df = pd.read_excel(file_path)
#         df.columns = [str(col).strip().lower() for col in df.columns]
        
#         if 'item name' in df.columns:
#             df.rename(columns={'item name': 'itemname'}, inplace=True)

#         required_columns = ['category', 'itemname', 'price']
#         for col in required_columns:
#             if col not in df.columns:
#                 raise KeyError(f"The required column '{col}' was not found in your Excel file. Please check the spelling and structure.")

#         df['price'] = pd.to_numeric(df['price'], errors='coerce')
#         df.dropna(subset=['itemname', 'price', 'category'], inplace=True)

#         _menu_df = df
#         _menu_as_string = _menu_df.to_json(orient='records', indent=4)
#         _menu_as_dict = _menu_df.groupby('category').apply(lambda x: x.to_dict('records')).to_dict()

#         print(f"✅ Menu loaded and processed successfully from {filename}")
        
#     except Exception as e:
#         print(f"❌ ERROR while loading menu: {e}")

# def get_menu_as_string():
#     """Returns the full menu as a JSON formatted string for the AI."""
#     return _menu_as_string

# def get_menu_as_dict():
#     """Returns the menu as a dictionary, grouped by category."""
#     return _menu_as_dict

# def get_item_details(item_name):
#     """Finds a specific item in the menu DataFrame and returns its details."""
#     if _menu_df is None:
#         return None
#     item = _menu_df[_menu_df['itemname'].str.lower() == item_name.lower()]
#     if not item.empty:
#         return item.iloc[0].to_dict()
#     return None

# # --- Initialize the menu when the module is first imported ---
# _initialize_menu()























# # data_manager.py Single Working Bot
# import pandas as pd
# import os
# import json

# # --- Private variables to store the loaded menu in different formats ---
# _menu_df = None
# _menu_as_string = None
# _menu_as_dict = None

# def _initialize_menu():
#     """
#     Internal function to load and process the menu from the correctly structured Excel file.
#     """
#     global _menu_df, _menu_as_string, _menu_as_dict
    
#     if _menu_df is not None:
#         return

#     filename = 'namasthe_hounslow_menu.xlsx'
#     file_path = os.path.join(os.path.dirname(__file__), 'data', filename)
    
#     try:
#         if not os.path.exists(file_path):
#             raise FileNotFoundError

#         df = pd.read_excel(file_path)
#         df.columns = [str(col).strip().lower() for col in df.columns]
        
#         if 'item name' in df.columns:
#             df.rename(columns={'item name': 'itemname'}, inplace=True)

#         required_columns = ['category', 'itemname', 'price']
#         for col in required_columns:
#             if col not in df.columns:
#                 raise KeyError(f"The required column '{col}' was not found in your Excel file. Please check the spelling and structure.")

#         df['price'] = pd.to_numeric(df['price'], errors='coerce')
#         df.dropna(subset=['itemname', 'price', 'category'], inplace=True)

#         _menu_df = df
#         _menu_as_string = _menu_df.to_json(orient='records', indent=4)
#         _menu_as_dict = _menu_df.groupby('category').apply(lambda x: x.to_dict('records')).to_dict()

#         print(f"✅ Menu loaded and processed successfully from {filename}")
        
#     except Exception as e:
#         print(f"❌ ERROR while loading menu: {e}")

# def get_menu_as_string():
#     """Returns the full menu as a JSON formatted string for the AI."""
#     return _menu_as_string

# def get_menu_as_dict():
#     """Returns the menu as a dictionary, grouped by category."""
#     return _menu_as_dict

# def get_item_details(item_name):
#     """Finds a specific item in the menu DataFrame and returns its details."""
#     if _menu_df is None:
#         return None
#     item = _menu_df[_menu_df['itemname'].str.lower() == item_name.lower()]
#     if not item.empty:
#         return item.iloc[0].to_dict()
#     return None

# # --- Initialize the menu when the module is first imported ---
# _initialize_menu()






















# # data_manager.py


# import pandas as pd
# import os
# import json

# _menu_df = None
# _menu_as_string = None
# _menu_as_dict = None

# def _initialize_menu():
#     """
#     Internal function to load and process the menu from the Excel file.
#     """
#     global _menu_df, _menu_as_string, _menu_as_dict
    
#     if _menu_df is not None:
#         return

#     filename = 'nutan_jewellers_menu.xlsx'
#     file_path = os.path.join(os.path.dirname(__file__), 'data', filename)
    
#     try:
#         if not os.path.exists(file_path):
#             raise FileNotFoundError(f"Menu file not found at {file_path}")

#         df = pd.read_excel(file_path)
#         df.columns = [str(col).strip().lower().replace(' ', '_') for col in df.columns]
        
#         if 'item_name' in df.columns:
#             df.rename(columns={'item_name': 'itemname'}, inplace=True)

#         required_columns = ['category', 'itemname', 'price']
#         for col in required_columns:
#             if col not in df.columns:
#                 raise KeyError(f"The required column '{col}' was not found in your Excel file.")

#         df['price'] = pd.to_numeric(df['price'], errors='coerce')
#         df.dropna(subset=['itemname', 'price', 'category'], inplace=True)
#         df['itemname'] = df['itemname'].astype(str).str.strip()
#         df['category'] = df['category'].astype(str).str.strip()

#         _menu_df = df
#         _menu_as_string = _menu_df.to_json(orient='records', indent=2)
        
#         _menu_as_dict = {
#             cat: data.to_dict('records') 
#             for cat, data in _menu_df.groupby('category')
#         }

#         print(f"✅ Menu loaded and processed successfully from {filename}")
        
#     except Exception as e:
#         print(f"❌ CRITICAL ERROR while loading menu: {e}")
#         _menu_df = pd.DataFrame()
#         _menu_as_dict = {}
#         _menu_as_string = "[]"

# def get_menu_as_string():
#     """Returns the full menu as a JSON formatted string for the AI."""
#     return _menu_as_string

# def get_menu_as_dict():
#     """Returns the menu as a dictionary, grouped by category."""
#     return _menu_as_dict

# def get_item_details(item_name):
#     """
#     Finds a specific item in the menu DataFrame (case-insensitive) and returns its details.
#     """
#     if _menu_df is None or _menu_df.empty: 
#         return None
        
#     item = _menu_df[_menu_df['itemname'].str.lower() == item_name.lower()]
    
#     if not item.empty:
#         return item.iloc[0].to_dict()
        
#     return None

# _initialize_menu()












## data_manager.py

import pandas as pd
import os
import json

_menu_df = None
_menu_as_string = None
_menu_as_dict = None

def _initialize_menu():
    """
    Internal function to load and process the menu from the Excel file.
    """
    global _menu_df, _menu_as_string, _menu_as_dict
    
    if _menu_df is not None:
        return

    # The menu file is expected to be in a 'data' subfolder
    filename = 'nutan_jewellers_menu.xlsx'
    file_path = os.path.join(os.path.dirname(__file__), 'data', filename)
    
    try:
        if not os.path.exists(file_path):
            # A more specific check for the menu file itself
            alt_path = os.path.join(os.path.dirname(__file__), filename)
            if not os.path.exists(alt_path):
                raise FileNotFoundError(f"Menu file not found at {file_path} or {alt_path}")
            file_path = alt_path

        df = pd.read_excel(file_path)
        # Standardize column names (e.g., "Item ID" -> "itemid")
        df.columns = [str(col).strip().lower().replace(' ', '_') for col in df.columns]
        
        # Accommodate a common alternative naming for 'itemname'
        if 'item_name' in df.columns:
            df.rename(columns={'item_name': 'itemname'}, inplace=True)

        # ✅ UPDATED: 'itemid' is now a required column
        required_columns = ['itemid', 'category', 'itemname', 'price']
        for col in required_columns:
            if col not in df.columns:
                raise KeyError(f"The required column '{col}' was not found in your Excel file.")

        # Clean and validate data
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df.dropna(subset=required_columns, inplace=True) # Check all required columns for missing data
        
        # ✅ UPDATED: Ensure all key columns are clean strings
        df['itemid'] = df['itemid'].astype(str).str.strip()
        df['itemname'] = df['itemname'].astype(str).str.strip()
        df['category'] = df['category'].astype(str).str.strip()

        _menu_df = df
        _menu_as_string = _menu_df.to_json(orient='records', indent=2)
        
        _menu_as_dict = {
            cat: data.to_dict('records') 
            for cat, data in _menu_df.groupby('category')
        }

        print(f"✅ Menu loaded and processed successfully from {filename}")
        
    except Exception as e:
        print(f"❌ CRITICAL ERROR while loading menu: {e}")
        _menu_df = pd.DataFrame()
        _menu_as_dict = {}
        _menu_as_string = "[]"

def get_menu_as_string():
    """Returns the full menu as a JSON formatted string for the AI."""
    return _menu_as_string

def get_menu_as_dict():
    """Returns the menu as a dictionary, grouped by category."""
    return _menu_as_dict

def get_item_details(identifier: str):
    """
    💡 UPGRADED: Finds an item by its unique ItemID (for buttons) or by its
    full ItemName (for text-based AI orders). Case-insensitive search.
    """
    if _menu_df is None or _menu_df.empty: 
        return None
        
    identifier_lower = identifier.lower()
    
    # 1. First, try to find a match by the unique 'itemid'
    item_by_id = _menu_df[_menu_df['itemid'].str.lower() == identifier_lower]
    if not item_by_id.empty:
        return item_by_id.iloc[0].to_dict()
        
    # 2. If not found, try to find a match by 'itemname' (for AI text orders)
    item_by_name = _menu_df[_menu_df['itemname'].str.lower() == identifier_lower]
    if not item_by_name.empty:
        return item_by_name.iloc[0].to_dict()
        
    # 3. If no match is found anywhere, return None
    return None

# This runs once when the bot starts
_initialize_menu()