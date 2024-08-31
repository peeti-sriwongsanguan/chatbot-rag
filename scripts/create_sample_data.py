import os

def create_sample_data():
    data = """Climate Change: An Overview

        Climate change refers to long-term shifts in global weather patterns and average temperatures. While climate fluctuations are natural, the rapid warming trend observed since the mid-20th century is primarily attributed to human activities.
        
        Causes of Climate Change:
        1. Greenhouse Gas Emissions: The burning of fossil fuels (coal, oil, and natural gas) releases carbon dioxide into the atmosphere, trapping heat and causing the greenhouse effect.
        2. Deforestation: Cutting down forests reduces the Earth's capacity to absorb carbon dioxide.
        3. Industrial Processes: Many industrial activities release greenhouse gases and other pollutants.
        4. Agriculture: Certain agricultural practices, including rice cultivation and livestock farming, contribute to methane emissions.
        
        Effects of Climate Change:
        1. Rising Temperatures: Global average temperatures have increased by about 1°C since pre-industrial times.
        2. Sea Level Rise: Melting ice caps and thermal expansion of oceans lead to rising sea levels, threatening coastal areas.
        3. Extreme Weather Events: Climate change is linked to an increase in the frequency and intensity of hurricanes, heatwaves, and droughts.
        4. Biodiversity Loss: Many species are struggling to adapt to rapidly changing habitats.
        
        Mitigation Strategies:
        1. Renewable Energy: Transitioning to clean energy sources like solar, wind, and hydroelectric power.
        2. Energy Efficiency: Improving energy efficiency in buildings, transportation, and industrial processes.
        3. Reforestation: Planting trees and protecting existing forests to absorb carbon dioxide.
        4. Sustainable Agriculture: Implementing farming practices that reduce emissions and increase carbon sequestration.
        
        International Efforts:
        The Paris Agreement, adopted in 2015, is a global treaty aimed at limiting global temperature increase to well below 2°C above pre-industrial levels. Countries have committed to reducing their greenhouse gas emissions and regularly reporting on their progress.
        
        Individual Actions:
        Individuals can contribute to fighting climate change by reducing energy consumption, using sustainable transportation, adopting plant-based diets, and supporting environmentally responsible businesses and policies.
        
        The Future:
        Addressing climate change requires global cooperation and swift action. While the challenges are significant, there are also opportunities for innovation in clean technologies and sustainable practices that can lead to a more resilient and equitable world.
        """

    # Ensure the data/raw directory exists
    os.makedirs('data/raw', exist_ok=True)

    # Write the data to a file
    with open('data/raw/climate_change.txt', 'w') as f:
        f.write(data)

    print("Sample data created successfully.")

if __name__ == "__main__":
    create_sample_data()