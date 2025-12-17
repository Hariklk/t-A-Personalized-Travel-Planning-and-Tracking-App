from typing import List, Dict

class TravelRecommendationSystem:
    def __init__(self, user_profile: Dict, trip_context: Dict, external_data: Dict):
        self.user_profile = user_profile
        self.trip_context = trip_context
        self.external_data = external_data
    
    def preprocess_data(self) -> Dict:
        """Prepare and normalize user + trip features."""
        return {
            "budget": self.user_profile.get("budget", 0) / 1000,
            "activities": self.encode_list(self.user_profile.get("activities", [])),
            "companions": self.trip_context.get("companions", "solo"),
            "duration": self.trip_context.get("duration_days", 7),
            "season": self.trip_context.get("season", "summer"),
            "dietary": self.user_profile.get("dietary"),
            "accessibility": self.user_profile.get("accessibility"),
            "language": self.user_profile.get("language", "English")
        }
    
    def encode_list(self, items: List[str]) -> Dict[str, int]:
        """Convert list of preferences into a simple feature dict."""
        return {item: 1 for item in items}
    
    def match_preferences(self, destination: str, features: Dict) -> float:
        """Score destination based on overlap with user preferences."""
        score = 0
        dest_info = self.external_data.get("destinations", {}).get(destination, {})
        
        for activity in features["activities"]:
            if activity in dest_info.get("activities", []):
                score += 1
        
  
        if dest_info.get("avg_cost", 0) <= self.user_profile.get("budget", 0):
            score += 1
        
        return score
    
    def collaborative_filter(self, destination: str) -> float:
        """Placeholder for collaborative filtering logic."""
        return 0.5
    
    def recommend_destinations(self, features: Dict) -> List[Dict]:
        """Generate ranked destination recommendations."""
        scores = {}
        for destination in self.external_data.get("destinations", {}):
            content_score = self.match_preferences(destination, features)
            collab_score = self.collaborative_filter(destination)
            scores[destination] = 0.6 * content_score + 0.4 * collab_score
        
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [
            {"destination": dest, "score": score, "explanation": self.explain_recommendation(dest)}
            for dest, score in ranked
        ]
    
    def explain_recommendation(self, destination: str) -> str:
        """Provide a human‑readable explanation for each recommendation."""
        return f"{destination} is suggested because it matches your activities and fits your budget."
    
    def get_recommendations(self) -> List[Dict]:
        """Public method to get recommendations in JSON‑style format."""
        features = self.preprocess_data()
        return self.recommend_destinations(features)
from typing import List, Dict

class TravelRecommendationSystem:
    def __init__(self, user_profile: Dict, trip_context: Dict, external_data: Dict):
        self.user_profile = user_profile
        self.trip_context = trip_context
        self.external_data = external_data
    
    def preprocess_data(self) -> Dict:
        """Prepare and normalize user + trip features."""
        return {
            "budget": self.user_profile.get("budget", 0) / 1000,
            "activities": self.encode_list(self.user_profile.get("activities", [])),
            "companions": self.trip_context.get("companions", "solo"),
            "duration": self.trip_context.get("duration_days", 7),
            "season": self.trip_context.get("season", "summer"),
            "dietary": self.user_profile.get("dietary"),
            "accessibility": self.user_profile.get("accessibility"),
            "language": self.user_profile.get("language", "English")
        }
    
    def encode_list(self, items: List[str]) -> Dict[str, int]:
        """Convert list of preferences into a simple feature dict."""
        return {item: 1 for item in items}
    
    def match_preferences(self, destination: str, features: Dict) -> float:
        """Score destination based on overlap with user preferences."""
        score = 0
        dest_info = self.external_data.get("destinations", {}).get(destination, {})
        
        # Activity overlap
        for activity in features["activities"]:
            if activity in dest_info.get("activities", []):
                score += 1
        
        # Budget fit
        if dest_info.get("avg_cost", 0) <= self.user_profile.get("budget", 0):
            score += 1
        
        return score
    
    def collaborative_filter(self, destination: str) -> float:
        """Placeholder for collaborative filtering logic."""
        return 0.5
    
    def recommend_destinations(self, features: Dict) -> List[Dict]:
        """Generate ranked destination recommendations."""
        scores = {}
        for destination in self.external_data.get("destinations", {}):
            content_score = self.match_preferences(destination, features)
            collab_score = self.collaborative_filter(destination)
            scores[destination] = 0.6 * content_score + 0.4 * collab_score
        
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [
            {"destination": dest, "score": score, "explanation": self.explain_recommendation(dest)}
            for dest, score in ranked
        ]
    
    def explain_recommendation(self, destination: str) -> str:
        """Provide a human‑readable explanation for each recommendation."""
        return f"{destination} is suggested because it matches your activities and fits your budget."
    
    def get_recommendations(self) -> List[Dict]:
        """Public method to get recommendations in JSON‑style format."""
        features = self.preprocess_data()
        return self.recommend_destinations(features)
from typing import List, Dict

class TravelRecommendationSystem:
    def __init__(self, user_profile: Dict, trip_context: Dict, external_data: Dict):
        self.user_profile = user_profile
        self.trip_context = trip_context
        self.external_data = external_data
    
    def preprocess_data(self) -> Dict:
        """Prepare and normalize user + trip features."""
        return {
            "budget": self.user_profile.get("budget", 0) / 1000,
            "activities": self.encode_list(self.user_profile.get("activities", [])),
            "companions": self.trip_context.get("companions", "solo"),
            "duration": self.trip_context.get("duration_days", 7),
            "season": self.trip_context.get("season", "summer"),
            "dietary": self.user_profile.get("dietary"),
            "accessibility": self.user_profile.get("accessibility"),
            "language": self.user_profile.get("language", "English")
        }
    
    def encode_list(self, items: List[str]) -> Dict[str, int]:
        """Convert list of preferences into a simple feature dict."""
        return {item: 1 for item in items}
    
    def match_preferences(self, destination: str, features: Dict) -> float:
        """Score destination based on overlap with user preferences."""
        score = 0
        dest_info = self.external_data.get("destinations", {}).get(destination, {})
        
        # Activity overlap
        for activity in features["activities"]:
            if activity in dest_info.get("activities", []):
                score += 1
        
        # Budget fit
        if dest_info.get("avg_cost", 0) <= self.user_profile.get("budget", 0):
            score += 1
        
        return score
    
    def collaborative_filter(self, destination: str) -> float:
        """Placeholder for collaborative filtering logic."""
        return 0.5
    
    def recommend_destinations(self, features: Dict) -> List[Dict]:
        """Generate ranked destination recommendations."""
        scores = {}
        for destination in self.external_data.get("destinations", {}):
            content_score = self.match_preferences(destination, features)
            collab_score = self.collaborative_filter(destination)
            scores[destination] = 0.6 * content_score + 0.4 * collab_score
        
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [
            {"destination": dest, "score": score, "explanation": self.explain_recommendation(dest)}
            for dest, score in ranked
        ]
    
    def explain_recommendation(self, destination: str) -> str:
        """Provide a human‑readable explanation for each recommendation."""
        return f"{destination} is suggested because it matches your activities and fits your budget."
    
    def get_recommendations(self) -> List[Dict]:
        """Public method to get recommendations in JSON‑style format."""
        features = self.preprocess_data()
        return self.recommend_destinations(features)
user_profile = {
    "name": "Hari",
    "age": 25,
    "budget": 2000,
    "activities": ["beach", "hiking", "food"],
    "dietary": "vegetarian",
    "accessibility": "wheelchair",
    "language": "English"
}

trip_context = {
    "season": "winter",
    "duration_days": 10,
    "companions": "friends"
}

external_data = {
    "destinations": {
        "Bali": {"activities": ["beach", "food"], "avg_cost": 1500},
        "Swiss Alps": {"activities": ["hiking", "skiing"], "avg_cost": 2500},
        "Tokyo": {"activities": ["food", "culture"], "avg_cost": 2200},
        "Kerala": {"activities": ["beach", "hiking"], "avg_cost": 1200}
    }
}

system = TravelRecommendationSystem(user_profile, trip_context, external_data)
recommendations = system.get_recommendations()



