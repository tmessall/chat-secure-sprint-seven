func sendCommandToFlaskServer(command: String) {
    guard let url = URL(string: "http://ip:5000/command") else { return }
    
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.addValue("application/json", forHTTPHeaderField: "Content-Type")
    
    let body: [String: Any] = ["command": command]
    request.httpBody = try? JSONSerialization.data(withJSONObject: body, options: [])

    let task = URLSession.shared.dataTask(with: request) { data, response, error in
        if let error = error {
            print("Error sending command: \(error)")
            return
        }
        // handling response
    }
    task.resume()
}
