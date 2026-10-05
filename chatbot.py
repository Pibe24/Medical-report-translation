
import streamlit as st
import ollama
import sys

def traduzione_testo_medico(testo_medico:str)->str:

    "Function that takes a medical report in italian and traslate it in italian but in a way"
    "that it is understandable for a patient"

    system_prompt = (
         "Agisci come un medico empatico, chiaro e un eccellente divulgatore scientifico. "
        "Il tuo compito è prendere un bollettino o referto medico tecnico e tradurlo in un "
        "linguaggio estremamente semplice, accessibile a una persona senza competenze mediche.\n\n"
        
        "Segui rigidamente queste regole:\n"
        "1. NON INVENTARE nulla: attieniti solo alle informazioni presenti nel testo fornito.\n"
        "2. NON FARE DIAGNOSI aggiuntive o prognosi che non siano esplicitamente scritte.\n"
        "3. Mantieni tutti i dati critici (es. valori numerici degli esami, nomi dei farmaci, dosaggi, date).\n"
        "4. Spiega i termini complessi o latini in modo semplice tra parentesi.\n"
        "5. Usa un tono rassicurante ma professionale.\n"
        "6. Dividi la risposta in tre sezioni chiare: 'Sintesi in parole semplici', 'Dettagli e Termini spiegati', 'Prossimi passi consigliati (se menzionati)'.\n"
        "7. Concludi SEMPRE con questo esatto disclaimer in grassetto: "
        "'*ATTENZIONE: Questa è una semplificazione automatica a scopo puramente informativo e non sostituisce in alcun modo il parere, la diagnosi o le indicazioni del tuo medico curante o dello specialista.*'"
    )

    try:
        # Chiamata a Ollama usando il modello open-source Llama 3.1
        risposta = ollama.chat(
            model='llama3.1',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': f"Ecco il bollettino medico da semplificare:\n\n{testo_medico}"}
            ],
            options={'temperature': 0.2}
        )
        return risposta['message']['content']
    except Exception as e:
        return f"Errore con Ollama: {e}.\nAssicurati che l'app Ollama sia aperta sul tuo PC."


def main():
    print("=" * 60)
    print("🩺 CHATBOT MEDICO OPEN-SOURCE (LINEA DI COMANDO) 🩺")
    print("=" * 60)
    print("Funziona 100% in locale, gratis e nel rispetto della privacy.")
    print("Digita 'esci' per chiudere il programma.\n")

    while True:
        print("\n" + "-" * 40)
        print("Incolla o digita il bollettino medico (premi INVIO due volte per confermare):")
        print("-" * 40)
        
        # Consente l'inserimento di testi su più righe (comodo per i copia-incolla lunghi)
        linee = []
        while True:
            linea = input()
            if linea == "":
                break
            linee.append(linea)
        
        testo_input = "\n".join(linee).strip()

        # Verifica comandi di uscita
        if testo_input.lower() in ['esci', 'exit', 'quit']:
            print("\nChiusura del chatbot. Buona giornata!")
            sys.exit()

        if not testo_input:
            print("[!] Testo vuoto. Riprova.")
            continue

        print("\n[...] Elaborazione e semplificazione in corso sul tuo hardware...")
        
        risultato = traduzione_testo_medico(testo_input)
        
        print("\n" + "=" * 60)
        print(risultato)
        print("=" * 60)

if __name__ == "__main__":
    main()


