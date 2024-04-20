
# The openAI API does not remeber our conversations, 
# hence, intizializing an array to store all of our msges ...
messages = []
while(1):
    # the record_text function converts speach into a text, to be stored in the text
    text = record_text()

    # we will now append this message to our conversation
    # GPT understands any converstation as a dictionary pair of --
        # role : who the message is by 
        # content : what the message actually is. 
    messages.append({"role": "user", "content": text})

    # Now once we have the message, we have to send it to Chatgpt, 
    # and we store that response as a string in response
    response = send_to_chatGPT(messages)

    # now we will convert this string reponse to speech, which would be heard by the users ...
    SpeakText(response)

    print(response)