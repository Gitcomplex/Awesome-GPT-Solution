css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://yamiyu.blob.core.windows.net/images/bot_icon.png?sp=r&st=2023-09-28T09:12:05Z&se=2023-09-28T17:12:05Z&sv=2022-11-02&sr=b&sig=CCEOpJVnFHEAd6qtUY%2F41qO%2BqJz5xAJ0O03qd%2B9IlvE%3D">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://yamiyu.blob.core.windows.net/images/user_icon.jpg?sp=r&st=2023-09-28T09:15:10Z&se=2023-09-28T17:15:10Z&sv=2022-11-02&sr=b&sig=KMwJxLTTwsTKVH5NZeh6aTDYT%2FgFZZdUcXhPpSkNDiY%3D">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''