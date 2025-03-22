# AllerScan
# =========
#
# A simple python script to help people who suffer from allergic reactions.
#
#

import pygame
import sys
import csv



# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 240, 320
#WIDTH, HEIGHT = 800, 600
ICON_WIDTH, ICON_HEIGHT = 75, 75 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (102,255,179)
RED = (255, 149, 128)
FONT = pygame.font.Font(None, 36)

# Load the icons for easy ID
celery = pygame.image.load("celery.png")  
celery = pygame.transform.scale(celery, (ICON_WIDTH, ICON_HEIGHT))
corn = pygame.image.load("corn.png")  
corn = pygame.transform.scale(corn, (ICON_WIDTH, ICON_HEIGHT))
crustaceans = pygame.image.load("crustaceans.png")  
crustaceans = pygame.transform.scale(crustaceans, (ICON_WIDTH, ICON_HEIGHT))
eggs = pygame.image.load("eggs.png")  
eggs = pygame.transform.scale(eggs, (ICON_WIDTH, ICON_HEIGHT))
fish = pygame.image.load("fish.png")  
fish = pygame.transform.scale(fish, (ICON_WIDTH, ICON_HEIGHT))
gluten = pygame.image.load("gluten.png")  
gluten = pygame.transform.scale(gluten, (ICON_WIDTH, ICON_HEIGHT))
lupin = pygame.image.load("lupin.png")  
lupin = pygame.transform.scale(lupin, (ICON_WIDTH, ICON_HEIGHT))
milk = pygame.image.load("milk.png")  
milk = pygame.transform.scale(milk, (ICON_WIDTH, ICON_HEIGHT))
molusc = pygame.image.load("molusc.png")  
molusc = pygame.transform.scale(molusc, (ICON_WIDTH, ICON_HEIGHT))
mustard = pygame.image.load("mustard.png")  
mustard = pygame.transform.scale(mustard, (ICON_WIDTH, ICON_HEIGHT))
notVeg = pygame.image.load("notVeg.jpg")  
notVeg = pygame.transform.scale(notVeg, (ICON_WIDTH, ICON_HEIGHT))
nuts = pygame.image.load("nuts.png")  
nuts = pygame.transform.scale(nuts, (ICON_WIDTH, ICON_HEIGHT))
peanut = pygame.image.load("peanut.png")  
peanut = pygame.transform.scale(peanut, (ICON_WIDTH, ICON_HEIGHT))
sesame = pygame.image.load("sesame.png")  
sesame = pygame.transform.scale(sesame, (ICON_WIDTH, ICON_HEIGHT))
soy = pygame.image.load("soy.png")  
soy = pygame.transform.scale(soy, (ICON_WIDTH, ICON_HEIGHT))
sulphite = pygame.image.load("sulphite.png")  
sulphite = pygame.transform.scale(sulphite, (ICON_WIDTH, ICON_HEIGHT))
oats = pygame.image.load("oats.png")  
oats = pygame.transform.scale(oats, (ICON_WIDTH, ICON_HEIGHT))
wheat = pygame.image.load("wheat.jpg")  
wheat = pygame.transform.scale(wheat, (ICON_WIDTH, ICON_HEIGHT))


# Allergen symbol positions
allergen_x_position = 0
allergen_x_spacing = 80
allergen_y_position = 55
allergen_y_spacing = 80
                

# Function to load food data from CSV
def load_food_data(csv_filename):
    food_data = {}
    try:
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            for row in reader:
             #   if len(row) < 17:
             #       continue  # Skip invalid rows
                print(row)
                barcode, name = row[1], row[2]
                allergens = {
                    "Peanuts": row[3], "Milk": row[4], "Eggs": row[5], "Gluten": row[6], "Fish": row[7],
                    "Crustaceans": row[8], "Mustard": row[9], "Soy": row[10], "Sesame": row[11], "Sulphites": row[12],
                    "Gelatin": row[13], "NonVegan": row[14], "NonVegetarian": row[15], "Wheat": row[16], "Oats": row [17]
                }
                food_data[barcode] = {"name": name, "allergens": allergens}
                
                
                
    except FileNotFoundError:
        print("CSV file not found!")
    return food_data

def check_symbol_positions():
    global allergen_x_position, allergen_y_position, allergen_x_spacing, allergen_y_spacing
    #print(allergen_y_position)
    if allergen_x_position > 160:
        allergen_x_position = 0
        allergen_y_position = allergen_y_position + allergen_y_spacing
    else:
        if allergen_y_position > 160:
            allergen_x_position = 0
            allergen_y_position = allergen_y_position + allergen_y_spacing
            
    

# Load food data
food_data = load_food_data("foods.csv")

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AllerScan")

# Input box
input_box = pygame.Rect(10, 10, 220, 40)
color_active = pygame.Color('dodgerblue2')
color_inactive = pygame.Color('lightskyblue3')
color = color_inactive
active = False
text = 'TEST'
result = None
allergen_warnings = []
product_name =""
running = True

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
      
        if event.type == pygame.QUIT:
            running = False
          
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
          
        if event.type == pygame.KEYDOWN:
          
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)

                    if test == "Quit":
                      running = False
                      pygame.quit()
                    
                    if text in food_data:
                        result = True
                        product_name = food_data[text]["name"]
                        allergen_warnings = [key for key, value in food_data[text]["allergens"].items() if value in ('1', '2')]
                    else:
                        result = False
                        allergen_warnings = []
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
    
   
                
    # Draw input box
    pygame.draw.rect(screen, color, input_box, 2)
    txt_surface = FONT.render(text, True, BLACK)
    screen.blit(txt_surface, (input_box.x + 10, input_box.y + 5))
    
    # Display result
  
    if result is not None:
        if result:
         #   pygame.draw.rect(screen, color, input_box, 2)
            #txt_surface = FONT.render(product_name, True, BLACK)
            #screen.blit(txt_surface, 10,30)

            font = pygame.font.Font('freesansbold.ttf', 32)
            Product_text = font.render(product_name, True, RED, WHITE)
            #screen.blit(Product_text, (WIDTH // 2, HEIGHT // 2))
            screen.blit(Product_text, (2, HEIGHT // 2))
            
            
            if allergen_warnings:
                #Allergen Warnings - Display suitable pics
                allergen_x_position = 0
                allergen_x_spacing = 80
                allergen_y_position = 55
                allergen_y_spacing = 140
                 
                
                 
                if "Celery" in allergen_warnings:
                    
                    check_symbol_positions()
                    screen.blit(celery, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
                    
                    
                if "Corn" in allergen_warnings:
                    
                    check_symbol_positions()
                    screen.blit(corn, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
                
                if "Eggs" in allergen_warnings:
                
                    check_symbol_positions()
                    screen.blit(eggs, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
                    
                if "Crustaceans" in allergen_warnings:
                
                    check_symbol_positions()
                    screen.blit(crustaceans, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
            
                if "Fish" in allergen_warnings:
                
                    check_symbol_positions()
                    screen.blit(fish, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
            
                if "Gluten" in allergen_warnings:
                    
                    check_symbol_positions()
                    screen.blit(gluten, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
                    
                if "Milk" in allergen_warnings:
                    
                    check_symbol_positions()
                    screen.blit(milk, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
                    
                if "Molusc" in allergen_warnings:
                    
                    check_symbol_positions()
                    screen.blit(molusc, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
                
                if "Mustard" in allergen_warnings:
                
                    check_symbol_positions()
                    screen.blit(mustard, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
                    
                if "Nuts" in allergen_warnings:
                
                    check_symbol_positions()
                    screen.blit(nuts, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
            
                if "NonVegetarian" in allergen_warnings:
                
                    check_symbol_positions()
                    screen.blit(notVeg, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
            
                if "Oats" in allergen_warnings:
                
                    check_symbol_positions()
                    screen.blit(oats, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
            
                if "Peanut" in allergen_warnings:
                
                    check_symbol_positions()
                    screen.blit(peanut, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
            
                if "Sesame" in allergen_warnings:
                
                    check_symbol_positions()
                    screen.blit(sesame, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
            
                if "Soy" in allergen_warnings:
                
                    check_symbol_positions()
                    screen.blit(soy, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
            
                if "Sulphite" in allergen_warnings:
                
                    check_symbol_positions()
                    screen.blit(sulphite, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
            
                if "Wheat" in allergen_warnings:
                
                    check_symbol_positions()
                    screen.blit(wheat, (allergen_x_position, allergen_y_position))
                    allergen_x_position = allergen_x_position + allergen_x_spacing
            


        else:
            pygame.draw.rect(screen, RED, (10, 60, 220, 250))
            not_known_text = FONT.render("Unknown Food", True, WHITE)
            screen.blit(not_known_text, (30, 120))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
