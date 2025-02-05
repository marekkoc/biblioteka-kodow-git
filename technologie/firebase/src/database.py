# src/database.py
import os
from typing import Dict, Any, Optional, List
from datetime import datetime

import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

class FirebaseManager:
    """Klasa do zarządzania operacjami na bazie Firebase."""
    
    def __init__(self, credentials_path: str):
        """
        Inicjalizacja połączenia z Firebase.
        
        Args:
            credentials_path: Ścieżka do pliku credentials JSON
        """
        if not firebase_admin._apps:  # Sprawdź czy Firebase nie jest już zainicjalizowany
            cred = credentials.Certificate(credentials_path)
            firebase_admin.initialize_app(cred)
        
        self.db = firestore.client()
        
    def add_data(self, collection: str, document_id: str, data: Dict[str, Any]) -> None:
        """
        Dodaje lub aktualizuje dokument w bazie.
        
        Args:
            collection: Nazwa kolekcji
            document_id: ID dokumentu
            data: Dane do zapisania
        """
        # Dodaj timestamp
        data['timestamp'] = firestore.SERVER_TIMESTAMP
        
        doc_ref = self.db.collection(collection).document(document_id)
        doc_ref.set(data)
        
    def get_data(self, collection: str, document_id: str) -> Optional[Dict[str, Any]]:
        """
        Pobiera dokument z bazy.
        
        Args:
            collection: Nazwa kolekcji
            document_id: ID dokumentu
            
        Returns:
            Dane dokumentu lub None jeśli nie istnieje
        """
        doc_ref = self.db.collection(collection).document(document_id)
        doc = doc_ref.get()
        
        return doc.to_dict() if doc.exists else None
        
    def query_collection(self, collection: str, field: str, operator: str, value: Any) -> List[Dict[str, Any]]:
        """
        Wyszukuje dokumenty spełniające warunek.
        
        Args:
            collection: Nazwa kolekcji
            field: Pole do przeszukania
            operator: Operator porównania ('==', '>', '<', '>=', '<=')
            value: Wartość do porównania
            
        Returns:
            Lista dokumentów spełniających warunek
        """
        docs = self.db.collection(collection).where(field, operator, value).stream()
        return [doc.to_dict() for doc in docs]

# Przykład użycia:
if __name__ == "__main__":
    load_dotenv()  # Załaduj zmienne środowiskowe
    
    # Inicjalizacja managera
    firebase = FirebaseManager(os.getenv('FIREBASE_CREDENTIALS_PATH'))
    
    # Przykładowe dane
    user_data = {
        'name': 'Anna Kowalska',
        'age': 28,
        'skills': ['Python', 'Data Science', 'Firebase']
    }
    
    # Dodaj dane
    firebase.add_data('users', 'anna.kowalska', user_data)
    
    # Pobierz dane
    user = firebase.get_data('users', 'anna.kowalska')
    print(f"Pobrane dane: {user}")
    
    # Wyszukaj użytkowników w określonym wieku
    users = firebase.query_collection('users', 'age', '>=', 25)
    print(f"Użytkownicy 25+: {users}")
