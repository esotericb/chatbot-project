function sendMessage() {
    const userInput = document.getElementById('user-input').value;

    if(!userInput) {
        alert("Please enter a query!");
        return;
    }

    fetch('/chat', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({query: userInput}),
    })
        .then(response => response.json())
        .then(data => {
            const chatOutput = document.getElementById('chat-output');

            // display user's message
            const userMessage = document.createElement('p');
            userMessage.className = 'user-message';
            userMessage.textContent = userInput;
            chatOutput.appendChild(userMessage);

            // display chatbot's response
            const botMessage = document.createElement('p');
            botMessage.className = 'bot-message';
            botMessage.textContent = data.response;  // Correctly use the 'response' from the server
            chatOutput.appendChild(botMessage);

            //reset the input field
            const inputField = document.getElementById('user-input');
            inputField.value = '';
            inputField.placeholder = 'Enter Your Query Here...';  // Reset the placeholder text



            chatOutput.scrollTop = chatOutput.scrollHeight;
        })

     .catch(error => console.error('Error:', error));
}