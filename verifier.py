import sys
import json
import os

def main():
    # Ler o resultado do TruffleHog da entrada padrão
    result = json.load(sys.stdin)

    # Verificar se o commit já foi verificado
    commit_sha = result.get("commit_sha")
    verification_state = load_verification_state()

    if commit_sha in verification_state:
        # O commit já foi verificado, não fazer nada
        valid = True
    else:
        # Realizar a verificação personalizada (por exemplo, verificar a chave privada)
        valid = perform_custom_verification(result)

        # Registrar o commit como verificado
        verification_state.append(commit_sha)
        save_verification_state(verification_state)

    # Saída do verificador
    verifier_output = {"valid": valid}

    # Imprimir a saída em JSON
    print(json.dumps(verifier_output))

def load_verification_state():
    # Carregar o estado de verificação a partir do arquivo de controle
    if os.path.exists("verifier_state.json"):
        with open("verifier_state.json", "r") as file:
            return json.load(file)
    else:
        return []

def save_verification_state(verification_state):
    # Salvar o estado de verificação de volta para o arquivo de controle
    with open("verifier_state.json", "w") as file:
        json.dump(verification_state, file)

def perform_custom_verification(result):
    # Realizar sua verificação personalizada aqui
    # Se a chave privada estiver presente no resultado, retorne False
    # Caso contrário, retorne True
    if "chave-privada.pem" in result.get("file"):
        return False
    else:
        return True

if __name__ == "__main__":
    main()
