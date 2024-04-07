import bs4
import requests
import pandas as pd
from openpyxl.styles import Border, Side
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Border, Side
import openpyxl
from openpyxl.packaging import workbook
# from openpyxl.styles import Border, Side
# from openpyxl import Workbook
# List of brand URLs
brand_urls = [
    ("10.or", "https://www.gadgets360.com/mobiles/10-or-phones"),
    ("Acer", "https://www.gadgets360.com/mobiles/acer-phones"),
    ("Adcom", "https://www.gadgets360.com/mobiles/adcom-phones"),
    ("Airtel", "https://www.gadgets360.com/mobiles/airtel-phones"),
    ("Alcatel", "https://www.gadgets360.com/mobiles/alcatel-phones"),
    ("Alpha", "https://www.gadgets360.com/mobiles/alpha-phones"),
    ("Amazon", "https://www.gadgets360.com/mobiles/amazon-phones"),
    ("AOC", "https://www.gadgets360.com/mobiles/aoc-phones"),
    ("Apple", "https://www.gadgets360.com/mobiles/apple-phones"),
    ("Aqua", "https://www.gadgets360.com/mobiles/aqua-phones"),
    ("Archos", "https://www.gadgets360.com/mobiles/archos-phones"),
    ("Asus", "https://www.gadgets360.com/mobiles/asus-phones"),
    ("Benq", "https://www.gadgets360.com/mobiles/benq-phones"),
    ("Billion", "https://www.gadgets360.com/mobiles/billion-phones"),
    ("Black Shark", "https://www.gadgets360.com/mobiles/black-shark-phones"),
    ("BlackBerry", "https://www.gadgets360.com/mobiles/blackberry-phones"),
    ("Blu", "https://www.gadgets360.com/mobiles/blu-phones"),
    ("BQ", "https://www.gadgets360.com/mobiles/bq-phones"),
    ("Byond", "https://www.gadgets360.com/mobiles/byond-phones"),
    ("Cat", "https://www.gadgets360.com/mobiles/cat-phones"),
    ("Celkon", "https://www.gadgets360.com/mobiles/celkon-phones"),
    ("Centric", "https://www.gadgets360.com/mobiles/centric-phones"),
    ("Champion Computers", "https://www.gadgets360.com/mobiles/champion-computers-phones"),
    ("ChampOne", "https://www.gadgets360.com/mobiles/champone-phones"),
    ("Cherry Mobile", "https://www.gadgets360.com/mobiles/cherry-mobile-phones"),
    ("Comio", "https://www.gadgets360.com/mobiles/comio-phones"),
    ("Coolpad", "https://www.gadgets360.com/mobiles/coolpad-phones"),
    ("Creo", "https://www.gadgets360.com/mobiles/creo-phones"),
    ("Croma", "https://www.gadgets360.com/mobiles/croma-phones"),
    ("Datawind", "https://www.gadgets360.com/mobiles/datawind-phones"),
    ("Detel", "https://www.gadgets360.com/mobiles/detel-phones"),
    ("Dizo", "https://www.gadgets360.com/mobiles/dizo-phones"),
    ("Docoss", "https://www.gadgets360.com/mobiles/docoss-phones"),
    ("Doogee", "https://www.gadgets360.com/mobiles/doogee-phones"),
    ("Elari", "https://www.gadgets360.com/mobiles/elari-phones"),
    ("Elephone", "https://www.gadgets360.com/mobiles/elephone-phones"),
    ("Energizer", "https://www.gadgets360.com/mobiles/energizer-phones"),
    ("Essential", "https://www.gadgets360.com/mobiles/essential-phones"),
    ("Evercoss", "https://www.gadgets360.com/mobiles/evercoss-phones"),
    ("Fairphone", "https://www.gadgets360.com/mobiles/fairphone-phones"),
    ("Flash", "https://www.gadgets360.com/mobiles/flash-phones"),
    ("Fly", "https://www.gadgets360.com/mobiles/fly-phones"),
    ("GeeksPhone", "https://www.gadgets360.com/mobiles/geeksphone-phones"),
    ("General Mobile", "https://www.gadgets360.com/mobiles/general-mobile-phones"),
    ("Gionee", "https://www.gadgets360.com/mobiles/gionee-phones"),
    ("Google", "https://www.gadgets360.com/mobiles/google-phones"),
    ("Hisense", "https://www.gadgets360.com/mobiles/hisense-phones"),
    ("Homtom", "https://www.gadgets360.com/mobiles/homtom-phones"),
    ("Honor", "https://www.gadgets360.com/mobiles/honor-phones"),
    ("HP", "https://www.gadgets360.com/mobiles/hp-phones"),
    ("HTC", "https://www.gadgets360.com/mobiles/htc-phones"),
    ("Huawei", "https://www.gadgets360.com/mobiles/huawei-phones"),
    ("Hyve", "https://www.gadgets360.com/mobiles/hyve-phones"),
    ("i-mobiles", "https://www.gadgets360.com/mobiles/i-mobiles-phones"),
    ("iBall", "https://www.gadgets360.com/mobiles/iball-phones"),
    ("iBerry", "https://www.gadgets360.com/mobiles/iberry-phones"),
    ("Idea", "https://www.gadgets360.com/mobiles/idea-phones"),
    ("Infinix", "https://www.gadgets360.com/mobiles/infinix-phones"),
    ("InFocus", "https://www.gadgets360.com/mobiles/infocus-phones"),
    ("Intex", "https://www.gadgets360.com/mobiles/intex-phones"),
    ("iQOO", "https://www.gadgets360.com/mobiles/iqoo-phones"),
    ("Itel", "https://www.gadgets360.com/mobiles/itel-phones"),
    ("iVoomi", "https://www.gadgets360.com/mobiles/ivoomi-phones"),
    ("Jio", "https://www.gadgets360.com/mobiles/jio-phones"),
    ("Jivi", "https://www.gadgets360.com/mobiles/jivi-phones"),
    ("Jolla", "https://www.gadgets360.com/mobiles/jolla-phones"),
    ("Josh Mobile", "https://www.gadgets360.com/mobiles/josh-mobile-phones"),
    ("Karbonn", "https://www.gadgets360.com/mobiles/karbonn-phones"),
    ("Kestrel", "https://www.gadgets360.com/mobiles/kestrel-phones"),
    ("Kodak", "https://www.gadgets360.com/mobiles/kodak-phones"),
    ("Kult", "https://www.gadgets360.com/mobiles/kult-phones"),
    ("Kyocera", "https://www.gadgets360.com/mobiles/kyocera-phones"),
    ("Land Rover", "https://www.gadgets360.com/mobiles/land-rover-phones"),
    ("Lava", "https://www.gadgets360.com/mobiles/lava-phones"),
    ("LeEco", "https://www.gadgets360.com/mobiles/leeco-phones"),
    ("Leica", "https://www.gadgets360.com/mobiles/leica-phones"),
    ("Lemon", "https://www.gadgets360.com/mobiles/lemon-phones"),
    ("Lenovo", "https://www.gadgets360.com/mobiles/lenovo-phones"),
    ("Lephone", "https://www.gadgets360.com/mobiles/lephone-phones"),
    ("Letv", "https://www.gadgets360.com/mobiles/letv-phones"),
    ("LG", "https://www.gadgets360.com/mobiles/lg-phones"),
    ("Lumigon", "https://www.gadgets360.com/mobiles/lumigon-phones"),
    ("Lyf", "https://www.gadgets360.com/mobiles/lyf-phones"),
    ("M-tech", "https://www.gadgets360.com/mobiles/m-tech-phones"),
    ("Mafe Mobile", "https://www.gadgets360.com/mobiles/mafe-mobile-phones"),
    ("Magicon", "https://www.gadgets360.com/mobiles/magicon-phones"),
    ("MarQ by Flipkart", "https://www.gadgets360.com/mobiles/marq-by-flipkart-phones"),
    ("Marshall", "https://www.gadgets360.com/mobiles/marshall-phones"),
    ("Maxx Mobile", "https://www.gadgets360.com/mobiles/maxx-mobile-phones"),
    ("Meizu", "https://www.gadgets360.com/mobiles/meizu-phones"),
    ("Mercury", "https://www.gadgets360.com/mobiles/mercury-phones"),
    ("Micromax", "https://www.gadgets360.com/mobiles/micromax-phones"),
    ("Microsoft", "https://www.gadgets360.com/mobiles/microsoft-phones"),
    ("Mitashi", "https://www.gadgets360.com/mobiles/mitashi-phones"),
    ("Mito", "https://www.gadgets360.com/mobiles/mito-phones"),
    ("Mobiistar", "https://www.gadgets360.com/mobiles/mobiistar-phones"),
    ("Moto", "https://www.gadgets360.com/mobiles/moto-phones"),
    ("Motorola", "https://www.gadgets360.com/mobiles/motorola-phones"),
    ("mPhone", "https://www.gadgets360.com/mobiles/mphone-phones"),
    ("MTS", "https://www.gadgets360.com/mobiles/mts-phones"),
    ("MyPhone", "https://www.gadgets360.com/mobiles/myphone-phones"),
    ("Namotel", "https://www.gadgets360.com/mobiles/namotel-phones"),
    ("Neffos", "https://www.gadgets360.com/mobiles/neffos-phones"),
    ("Nexian", "https://www.gadgets360.com/mobiles/nexian-phones"),
    ("Nextbit", "https://www.gadgets360.com/mobiles/nextbit-phones"),
    ("Nokia", "https://www.gadgets360.com/mobiles/nokia-phones"),
    ("Nothing", "https://www.gadgets360.com/mobiles/nothing-phones"),
    ("Nubia", "https://www.gadgets360.com/mobiles/nubia-phones"),
    ("Nuu Mobile", "https://www.gadgets360.com/mobiles/nuu-mobile-phones"),
    ("Obi", "https://www.gadgets360.com/mobiles/obi-phones"),
    ("Obi Worldphone", "https://www.gadgets360.com/mobiles/obi-worldphone-phones"),
    ("OnePlus", "https://www.gadgets360.com/mobiles/oneplus-phones"),
    ("Onida", "https://www.gadgets360.com/mobiles/onida-phones"),
    ("Oplus", "https://www.gadgets360.com/mobiles/oplus-phones"),
    ("Oppo", "https://www.gadgets360.com/mobiles/oppo-phones"),
    ("Oukitel", "https://www.gadgets360.com/mobiles/oukitel-phones"),
    ("Panasonic", "https://www.gadgets360.com/mobiles/panasonic-phones"),
    ("Pantel", "https://www.gadgets360.com/mobiles/pantel-phones"),
    ("Pepsi", "https://www.gadgets360.com/mobiles/pepsi-phones"),
    ("Phicomm", "https://www.gadgets360.com/mobiles/phicomm-phones"),
    ("Philips", "https://www.gadgets360.com/mobiles/philips-phones"),
    ("Poco", "https://www.gadgets360.com/mobiles/poco-phones"),
    ("Polaroid", "https://www.gadgets360.com/mobiles/polaroid-phones"),
    ("Prestigio", "https://www.gadgets360.com/mobiles/prestigio-phones"),
    ("Qiku", "https://www.gadgets360.com/mobiles/qiku-phones"),
    ("QiKU", "https://www.gadgets360.com/mobiles/qiku-phones"),
    ("Qmobile", "https://www.gadgets360.com/mobiles/qmobile-phones"),
    ("Qtek", "https://www.gadgets360.com/mobiles/qtek-phones"),
    ("Rage", "https://www.gadgets360.com/mobiles/rage-phones"),
    ("Reach", "https://www.gadgets360.com/mobiles/reach-phones"),
    ("Razer", "https://www.gadgets360.com/mobiles/razer-phones"),
    ("Realme", "https://www.gadgets360.com/mobiles/realme-phones"),
    ("Redmi", "https://www.gadgets360.com/mobiles/redmi-phones"),
    ("Ringing Bells", "https://www.gadgets360.com/mobiles/ringing-bells-phones"),
    ("Rivo", "https://www.gadgets360.com/mobiles/rivo-phones"),
    ("Rokea", "https://www.gadgets360.com/mobiles/rokea-phones"),
    ("Salora", "https://www.gadgets360.com/mobiles/salora-phones"),
    ("Samsung", "https://www.gadgets360.com/mobiles/samsung-phones"),
    ("Sansui", "https://www.gadgets360.com/mobiles/sansui-phones"),
    ("Sanyo", "https://www.gadgets360.com/mobiles/sanyo-phones"),
    ("Sendo", "https://www.gadgets360.com/mobiles/sendo-phones"),
    ("Sharp", "https://www.gadgets360.com/mobiles/sharp-phones"),
    ("Siemens", "https://www.gadgets360.com/mobiles/siemens-phones"),
    ("Sigma", "https://www.gadgets360.com/mobiles/sigma-phones"),
    ("Sirin Labs", "https://www.gadgets360.com/mobiles/sirin-labs-phones"),
    ("Smartisan", "https://www.gadgets360.com/mobiles/smartisan-phones"),
    ("Smartron", "https://www.gadgets360.com/mobiles/smartron-phones"),
    ("Snexian", "https://www.gadgets360.com/mobiles/snexian-phones"),
    ("Snom", "https://www.gadgets360.com/mobiles/snom-phones"),
    ("Sonim", "https://www.gadgets360.com/mobiles/sonim-phones"),
    ("Sony", "https://www.gadgets360.com/mobiles/sony-phones"),
    ("Spice", "https://www.gadgets360.com/mobiles/spice-phones"),
    ("Swipe", "https://www.gadgets360.com/mobiles/swipe-phones"),
    ("T-Mobile", "https://www.gadgets360.com/mobiles/t-mobile-phones"),
    ("TCL", "https://www.gadgets360.com/mobiles/tcl-phones"),
    ("Tecno", "https://www.gadgets360.com/mobiles/tecno-phones"),
    ("Tel.Me.", "https://www.gadgets360.com/mobiles/tel-me-phones"),
    ("Telenor", "https://www.gadgets360.com/mobiles/telenor-phones"),
    ("Telit", "https://www.gadgets360.com/mobiles/telit-phones"),
    ("Thuraya", "https://www.gadgets360.com/mobiles/thuraya-phones"),
    ("TP-Link", "https://www.gadgets360.com/mobiles/tp-link-phones"),
    ("Turing", "https://www.gadgets360.com/mobiles/turing-phones"),
    ("Ulefone", "https://www.gadgets360.com/mobiles/ulefone-phones"),
    ("Umi", "https://www.gadgets360.com/mobiles/umi-phones"),
    ("Unihertz", "https://www.gadgets360.com/mobiles/unihertz-phones"),
    ("Uniscope", "https://www.gadgets360.com/mobiles/uniscope-phones"),
    ("Unistar", "https://www.gadgets360.com/mobiles/unistar-phones"),
    ("Usha", "https://www.gadgets360.com/mobiles/usha-phones"),
    ("Vaio", "https://www.gadgets360.com/mobiles/vaio-phones"),
    ("Verizon", "https://www.gadgets360.com/mobiles/verizon-phones"),
    ("Vertu", "https://www.gadgets360.com/mobiles/vertu-phones"),
    ("Videocon", "https://www.gadgets360.com/mobiles/videocon-phones"),
    ("ViewSonic", "https://www.gadgets360.com/mobiles/viewsonic-phones"),
    ("Vivo", "https://www.gadgets360.com/mobiles/vivo-phones"),
    ("Vodafone", "https://www.gadgets360.com/mobiles/vodafone-phones"),
    ("Voto", "https://www.gadgets360.com/mobiles/voto-phones"),
    ("Wiko", "https://www.gadgets360.com/mobiles/wiko-phones"),
    ("Wiio", "https://www.gadgets360.com/mobiles/wiio-phones"),
    ("Wileyfox", "https://www.gadgets360.com/mobiles/wileyfox-phones"),
    ("WingFone", "https://www.gadgets360.com/mobiles/wingfone-phones"),
    ("Wynncom", "https://www.gadgets360.com/mobiles/wynncom-phones"),
    ("Xiaomi", "https://www.gadgets360.com/mobiles/xiaomi-phones"),
    ("Xolo", "https://www.gadgets360.com/mobiles/xolo-phones"),
    ("Yezz", "https://www.gadgets360.com/mobiles/yezz-phones"),
    ("Yota", "https://www.gadgets360.com/mobiles/yota-phones"),
    ("YU", "https://www.gadgets360.com/mobiles/yu-phones"),
    ("Yxtel", "https://www.gadgets360.com/mobiles/yxtel-phones"),
    ("Zebra", "https://www.gadgets360.com/mobiles/zebra-phones"),
    ("Zen", "https://www.gadgets360.com/mobiles/zen-phones"),
    ("Ziox", "https://www.gadgets360.com/mobiles/ziox-phones"),
    ("Zopo", "https://www.gadgets360.com/mobiles/zopo-phones"),
    ("ZTE", "https://www.gadgets360.com/mobiles/zte-phones"),
    ("Zync", "https://www.gadgets360.com/mobiles/zync-phones")
]
all_phone_names = []

# Loop through each brand URL
# Create an ExcelWriter object
with pd.ExcelWriter('mobile_phones.xlsx', engine='openpyxl') as writer:
    for brand_name, brand_url in brand_urls:
        brand_page = requests.get(brand_url)
        brand_soup = bs4.BeautifulSoup(brand_page.content, 'html.parser')

        # Find all mobile phones for the current brand
        mobile_phones = brand_soup.select('.nlist .rvw-title strong')

        # Extract phone names for the current brand
        phone_names = [phone.get_text().strip() for phone in mobile_phones]

        # Convert phone_names to a list
        phone_names = list(phone_names)

        # Create a DataFrame for the current brand
        df = pd.DataFrame({'S.no': range(1, len(phone_names) + 1),
                           'Model.no': phone_names,
                           '': [''] * len(phone_names),
                           '': [''] * len(phone_names),
                           '': [''] * len(phone_names)})

        # Write the DataFrame to Excel with the brand name as the sheet name
        df.to_excel(writer, sheet_name=brand_name, index=False, startrow=1, startcol=1)

        # Get the workbook and the worksheet
        workbook = writer.book

        try:
            worksheet = writer.sheets[brand_name]

            def apply_borders(worksheet, cell_range):
                border_style = Border(left=Side(border_style='thin'),
                                      right=Side(border_style='thin'),
                                      top=Side(border_style='thin'),
                                      bottom=Side(border_style='thin'))

                for row in worksheet[cell_range]:
                    for cell in row:
                        cell.border = border_style

            # Apply borders to the entire DataFrame
            
            apply_borders(worksheet, f"A1:E{len(phone_names) + 1}")

            # Set column widths
            for col in worksheet.columns:
                max_length = 0
                column = col[0].column_letter  # Get the column name
                for cell in col:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(cell.value)
                    except:
                        pass
                adjusted_width = (max_length + 2) * 1.2
                worksheet.column_dimensions[column].width = adjusted_width

            # Add column headings
            headings = ['S.no', 'Model.no', '', '', '']
            for idx, heading in enumerate(headings, start=1):
                worksheet.cell(row=1, column=idx, value=heading)

        except KeyError:
            print(f"No data found for {brand_name}. Skipping...")

print("Excel file 'mobile_phones.xlsx' created.")
