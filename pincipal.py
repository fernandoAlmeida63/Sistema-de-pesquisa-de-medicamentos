from binary_tree import BinaryTree

def main():
    tree = BinaryTree()

    # Adicionando sintomas e medicamentos à árvore
    sintomas_e_medicamentos = [
        ("dor de cabeça", "Paracetamol para dor de cabeça", "Dor ou desconforto na cabeça ou pescoço."),
        ("febre", "Dipirona", "Elevação temporária da temperatura do corpo, geralmente devido a uma infecção."),
        ("tosse", "Xarope para tosse", "Reflexo protetor que ajuda a limpar as vias respiratórias de irritantes."),
        ("dor de garganta", "Pastilhas para garganta", "Dor ou irritação na garganta, geralmente causada por infecção viral ou bacteriana."),
        ("corrimento nasal", "Descongestionante nasal", "Secreção excessiva de muco pelo nariz."),
        ("fadiga", "Vitaminas", "Sensação de cansaço extremo e falta de energia."),
        ("náusea", "Dimenidrinato", "Sensação de enjoo com vontade de vomitar."),
        ("dores musculares", "Analgésico", "Dor nos músculos, frequentemente causada por esforço excessivo ou inflamação."),
        ("dor abdominal", "Antiespasmódico", "Dor ou desconforto na região do abdômen."),
        ("diarreia", "Antidiarreico", "Fezes soltas e aquosas, muitas vezes devido a uma infecção gastrointestinal."),
        ("constipação", "Laxante", "Dificuldade para evacuar ou evacuações pouco frequentes."),
        ("azia", "Antiácido", "Queimação no estômago ou no peito devido ao refluxo de ácido gástrico."),
        ("dor nas articulações", "Anti-inflamatório", "Dor ou inflamação nas articulações, frequentemente associada a artrite."),
        ("ansiedade", "Ansiolítico", "Sensação de preocupação, nervosismo ou medo intensa."),
        ("insônia", "Melatonina", "Dificuldade para adormecer ou manter o sono."),
        ("tontura", "Vertigoheel", "Sensação de desorientação ou falta de equilíbrio."),
        ("alergia", "Antialérgico", "Reação exagerada do sistema imunológico a substâncias inofensivas."),
        ("prurido", "Creme de cortisona", "Coceira intensa na pele."),
        ("infecção urinária", "Antibiótico", "Infecção em qualquer parte do sistema urinário, geralmente na bexiga ou uretra."),
        ("hipertensão", "Anti-hipertensivo", "Pressão arterial anormalmente alta."),
        ("diabetes", "Insulina", "Doença crônica que afeta a forma como o corpo processa o açúcar no sangue."),
        ("asma", "Broncodilatador", "Doença crônica que causa inflamação e estreitamento das vias aéreas."),
        ("bronquite", "Corticosteroide inalatório", "Inflamação dos brônquios, causando tosse persistente e produção de muco."),
        ("hipotireoidismo", "Levotiroxina", "Condição em que a glândula tireoide não produz hormônio tireoidiano suficiente."),
        ("hipertireoidismo", "Metimazol", "Condição em que a glândula tireoide produz hormônio tireoidiano em excesso."),
        ("gastrite", "Inibidor de bomba de prótons", "Inflamação do revestimento do estômago."),
        ("hemorroida", "Pomada anti-hemorroidária", "Veias inchadas no ânus e na parte inferior do reto."),
        ("problemas digestivos", "Digestivo", "Distúrbios que afetam a digestão, como indigestão ou refluxo ácido."),
        ("problemas de pele", "Pomada antibiótica", "Afecções que afetam a pele, como infecções ou inflamações."),
        ("infecção por fungos", "Antifúngico", "Infecção causada por fungos, frequentemente afetando a pele, unhas ou mucosas."),
        ("hiperlipidemia", "Estatina", "Níveis elevados de lipídios no sangue, aumentando o risco de doenças cardíacas."),
        ("osteoporose", "Bifosfonato", "Doença que enfraquece os ossos, tornando-os mais suscetíveis a fraturas."),
        ("gripe", "Antigripal", "Infecção viral que causa febre, tosse, dores no corpo e fadiga."),
        ("mau hálito", "Antisséptico bucal", "Odor desagradável da boca, geralmente causado por má higiene bucal."),
        ("dificuldade respiratória", "Inalador", "Dificuldade para respirar devido a condições como asma ou doença pulmonar obstrutiva crônica (DPOC)."),
        ("zumbido no ouvido", "Suplemento de ginkgo biloba", "Percepção de ruído ou zumbido nos ouvidos."),
        ("queda de cabelo", "Minoxidil", "Perda de cabelo, frequentemente causada por fatores genéticos ou hormonais."),
        ("desidratação", "Soro de reidratação oral", "Perda excessiva de água e eletrólitos do corpo."),
        ("dor de dente", "Analgésico dental", "Dor em um dente ou ao redor dele, frequentemente causada por cáries ou infecção."),
        ("vômito", "Anti-emético", "Expulsão forçada do conteúdo do estômago pela boca."),
        ("cãibras", "Suplemento de magnésio", "Contrações dolorosas e involuntárias dos músculos."),
        ("ressaca", "Reidratante oral", "Conjunto de sintomas desagradáveis após consumo excessivo de álcool."),
        ("ansiedade", "Ansiolítico", "Sensação de preocupação, nervosismo ou medo intensa."),
        ("epistaxe", "Cauterização nasal", "Sangramento do nariz."),
        ("anemia", "Suplemento de ferro", "Deficiência de glóbulos vermelhos ou hemoglobina no sangue."),
        ("encefalite", "Antiviral", "Inflamação do cérebro, geralmente causada por infecção viral."),
        ("malária", "Antimalárico", "Doença transmitida por mosquitos, causando febre alta e calafrios."),
        ("hepatite", "Medicamento antiviral", "Inflamação do fígado, frequentemente causada por infecção viral."),
        ("tuberculose", "Antibiótico específico para tuberculose", "Doença infecciosa que afeta principalmente os pulmões."),
    ]

    for symptom, medication, description in sintomas_e_medicamentos:
        tree.add(symptom, medication, description)  # Adiciona os dados à árvore

    while True:
        # Solicitar os sintomas do usuário
        symptoms = tree.ask_symptoms()  # Chama a função para perguntar os sintomas ao usuário

        # Obter recomendações de medicamentos
        recommendations = tree.get_medication_recommendation(symptoms)  # Obtém as recomendações de medicamentos

        if recommendations:
            print("\nRecomendações de medicamentos com base nos seus sintomas:")
            for recommendation in recommendations:
                print(recommendation)  # Exibe as recomendações de medicamentos
        else:
            print("\nNenhuma recomendação de medicamento encontrada para os sintomas fornecidos.")

        # Perguntar ao usuário se deseja reiniciar a pesquisa
        restart = input("\nDeseja reiniciar a pesquisa? (sim/não): ").strip().lower()
        if restart != 'sim':
            print("Finalizando o programa.")
            break  # Encerra o loop e finaliza o programa

if __name__ == "__main__":
    main()
