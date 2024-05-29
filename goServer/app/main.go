package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"strconv"
	"sync"
	"io"
)


var attacks map[int]Attack
var lastID int = 0;
var myMutex sync.Mutex

func main() {
	attacks = load_from_json("attacks.json", 30)

	http.HandleFunc("/", hello)
	http.Handle("/all-attacks", http.HandlerFunc(allAttacks))
	http.Handle("/attack", http.HandlerFunc(getSingleAttack))
	http.Handle("/add-attack", http.HandlerFunc(addAttack))
	http.Handle("/delete", http.HandlerFunc(deleteAttack))
	http.ListenAndServe(":3000", nil)
	fmt.Println("Serwer nasłuchuje na porcie 3000")
}

func load_from_json(jsonFile string, n int) map[int]Attack {
	file, err := os.ReadFile(jsonFile)
	if err != nil {
		panic("Błąd podczas odczytu pliku")
	}

	var attacksArr []Attack
	err = json.Unmarshal(file, &attacksArr)
	if err != nil {
		panic("Błąd podczas analizowania danych JSON")
	}

	if n < len(attacksArr) {
		attacksArr = attacksArr[:n]
	}

	result := make(map[int]Attack)

	for i := range attacksArr {
		result[i+1] = attacksArr[i]
		lastID++
	}

	return result
}

// Server handlers
func hello(w http.ResponseWriter, req *http.Request) {
	fmt.Fprintf(w, "Hello World!!!")
}

func allAttacks(w http.ResponseWriter, req *http.Request) {
	myMutex.Lock()
	defer myMutex.Unlock()

	jsonData, err := json.Marshal(attacks)
	if err != nil {
		http.Error(w, "Błąd podczas konwersji danych na JSON", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(jsonData)
}

func getSingleAttack(w http.ResponseWriter, req *http.Request) {
	myMutex.Lock()
	defer myMutex.Unlock()

	urlParameters, ok := req.URL.Query()["id"]

	if !ok || len(urlParameters[0]) < 1 {
		http.Error(w, "Missing id parameter", http.StatusBadRequest)
		return
	}

	id, err := strconv.Atoi(urlParameters[0])

	if err != nil {
		http.Error(w, "Bad id type", http.StatusBadRequest)
		return
	}

	if value, exists := attacks[id]; exists {
		jsonData, err := json.Marshal(value)
		if err != nil {
			http.Error(w, "Błąd podczas konwersji danych na JSON", http.StatusInternalServerError)
			return
		} else {
			w.Header().Set("Content-Type", "application/json")
			w.Write(jsonData)
			return
		}
	} else {
		http.Error(w, "Atak o podanym ID nie istnieje", http.StatusNoContent)
	}
}

func addAttack(w http.ResponseWriter, r *http.Request) {
	myMutex.Lock()
	defer myMutex.Unlock()
	
	body, err := io.ReadAll(r.Body)
	if err != nil {
			http.Error(w, "Błąd odczytu treści żądania", http.StatusBadRequest)
			return
	}
	defer r.Body.Close()

	var newAttack Attack
	err = json.Unmarshal(body, &newAttack)
	if err != nil {
			http.Error(w, "Błąd dekodowania JSON", http.StatusBadRequest)
			return
	}

	lastID++
	attacks[lastID] = newAttack

	w.WriteHeader(http.StatusCreated)
}



func deleteAttack(w http.ResponseWriter, req *http.Request) {
	myMutex.Lock()
	defer myMutex.Unlock()
	urlParameters, ok := req.URL.Query()["id"]

	if !ok || len(urlParameters[0]) < 1 {
		http.Error(w, "Missing id parameter", http.StatusBadRequest)
		return
	}

	id, err := strconv.Atoi(urlParameters[0])

	if err != nil {
		http.Error(w, "Bad id type", http.StatusBadRequest)
		return
	}

	delete(attacks, id)
	w.WriteHeader(http.StatusOK)
}

// Attack
type Attack struct {
	Date     *string `json:"date"`
	Name     *string `json:"name"`
	Type     *string `json:"type"`
	Country  *string `json:"country"`
	Area     *string `json:"area"`
	Activity *string `json:"activity"`
	Injury   *string `json:"injury"`
}