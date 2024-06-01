function sendMessage(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const chatThread = document.querySelector(".chat-thread");

    function scrollToBottom() {
        chatThread.scrollTop = chatThread.scrollHeight; // Automatically scroll to the bottom of the chat container
    }

    // Get the input field and its value
    let inputField = document.querySelector('.chat-window-message');
    let message = inputField.value.trim();

    // Check if the message is not empty
    if (message) {
        // Create a new list item
        let newMessage = document.createElement('li');
        newMessage.textContent = message;

        // Append the message to the chat thread
        document.getElementById('chat-thread').appendChild(newMessage);

        // Clear the input field after sending
        inputField.value = '';

        scrollToBottom(); // Scroll chat thread to the newest message
    }
}


// Optional: handle the message input with Enter key
document.querySelector('.chat-window-message').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage(e);
    }
});

