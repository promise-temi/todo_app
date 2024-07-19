<template>
    <div>
      <form @submit.prevent="sendEmail">
        <input type="text" v-model="name" placeholder="Votre Nom" />
        <input type="email" v-model="email" placeholder="Votre Email" />
        <textarea v-model="message" placeholder="Votre Message"></textarea>
        <button type="submit">Envoyer</button>
      </form>
    </div>
  </template>
  
  <script>
  import emailjs from 'emailjs-com';
  
  export default {
    data() {
      return {
        name: '',
        email: '',
        message: '',
      };
    },
    methods: {
      sendEmail() {
        const templateParams = {
          name: this.name,
          email: this.email,
          message: this.message,
        };
  
        emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', templateParams, 'YOUR_USER_ID')
          .then((response) => {
            console.log('SUCCESS!', response.status, response.text);
          }, (error) => {
            console.log('FAILED...', error);
          });
      },
    },
  };
  </script>
  