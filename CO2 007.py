import inquirer

# Dados de emissão de CO2 dos veículos
co2_emissions = {
    "Híbrido": 104,
    "Elétrico": 0,
    "Combustão": 192,
    "Hidrogênio": 0
}

# Eficiência do combustível em km/litro
media_combustivel = {
    "Híbrido": 20,
    "Elétrico": 0,
    "Combustão": 13.5,
    "Hidrogênio": 0
}

# Fator de emissão de CO2 em g/km
co2_fator = {
    "Híbrido": 0.000104,
    "Elétrico": 0,
    "Combustão": 0.000192,
    "Hidrogênio": 0
}

# Pergunta ao usuário quais tipos de veículo ele deseja escolher (permite múltipla escolha)
questoes = [
    inquirer.Checkbox(
        "vehicle_types",
        message="Quais tipos de veículos você deseja escolher?",
        choices=["Híbrido", "Elétrico", "Combustão", "Hidrogênio"],
    ),
    inquirer.Text(
        "distance",
        message="Qual a distância que você deseja percorrer (em km)?",
        validate=lambda _, x: x.isdigit() or "Por favor, insira um número inteiro.",
    ),
]

answers = inquirer.prompt(questoes)

# Calcula a média geral de emissão de CO2 dos veículos escolhidos pelo usuário
distance = int(answers["distance"])
selected_vehicle_types = answers["vehicle_types"]

if not selected_vehicle_types:
    print("Você não selecionou nenhum tipo de veículo.")
else:
    total_distance = distance * len(selected_vehicle_types)

    total_co2_emission = sum(
        [
            (distance / media_combustivel[vehicle_type]) * co2_fator[vehicle_type] * distance
            for vehicle_type in selected_vehicle_types
        ]
    )

    average_co2_emission = total_co2_emission / total_distance

    print(f"A média geral de emissão de CO2 dos veículos escolhidos é {average_co2_emission:.2f} g/km.")

    total_co2_emission_full_distance = sum(
        [
            (total_distance / media_combustivel[vehicle_type]) * co2_fator[vehicle_type] * total_distance
            for vehicle_type in selected_vehicle_types
        ]
    )

    total_co2_emission_kg = total_co2_emission_full_distance / 1000  # Converter para kg

    print(f"A emissão total de CO2 para o percurso completo de {total_distance} km é {total_co2_emission_full_distance:.2f} g.")
    print(f"A emissão total de CO2 para o percurso completo de {total_distance} km é {total_co2_emission_kg:.2f} kg.")
