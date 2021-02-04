## How to install Messaging Component

#### **Step 1**: Download the wheel file using "https://github.com/tavroi/MessagingComponents/raw/main/dist/MessagingComponents-0.1.0-py3-none-any.whl".
#### **Step 2**: open a cmd and change the working directory to folder where you have downloaded the wheel file.
#### **Step 3**: Pip install MessagingComponents-0.1.0-py3-none-any.whl

## How to use Different components

### How to create quick replies:
##### How to import create_quick_replies using the following commands.
        from MessagingComponents import create_quick_replies
##### **This function takes 3 parameters**:
##### **a**. channel: This parameter should contain channel name from which request is coming. e.g. facebook, rest.
##### **b**. text: This parameter should contain text which will be send with quick replies. e.g. "Choose from the following."
##### **c**. quick_reply_data: It contains the content of quick reply buttons. e.g.
    [
        {
            "title": "🔎 Explore Products",
            "action_type": "postback",
            "payload": "/explore_products",
            "image_url": "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/emojidex/112/left-pointing-magnifying-glass_1f50d.png"
        }
    ]

### How to create carousel:
##### How to import create_carousel using the following commands.
        from MessagingComponents import create_carousel
##### **This function takes 2 parameters**:
##### **a**. channel: This parameter should contain channel name from which request is coming. e.g. facebook, rest.
##### **b**. carousel_data: It contains the content of carousel. e.g.
    [
        {
            "image_url": "https://civilcops-assets.nyc3.digitaloceanspaces.com/power-gummies/Review1.png",
            "title": "It has totally transformed my hair from weak and scanty to strong & voluminous.",
            "caption": "Read the full review by clicking the button below",
            "default": "",
            "button":  [
                            {
                            "type": "web_url",
                            "url": https://abc.com/cart.php?product_id={products[index]['id']}",
                            "title": "Show"
                            }
                        ]
        }
    ]

### How to create carousel:
##### How to import create_carousel using the following commands.
        from MessagingComponents import create_carousel
##### **This function takes 3 parameters**:
##### **a**. channel: This parameter should contain channel name from which request is coming. e.g. facebook, rest.
##### **b**. text: This parameter should contain text which will be send with quick replies. e.g. "Choose from the following."
##### **c**. button_data: It contains the content of button. e.g.
        [{
            "title": "Go to Cart",
            "url": f"{PROJECT_BASE_URL}cart.php?cart=true"
        }]
