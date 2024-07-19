<template>
    <div class="sign-in-page-bg">
        <span class="for-show-s-in-be-well">hello</span>
        <SignIn></SignIn>
    </div>
    
</template>
<script>

import SignIn from '@/components/SignIn.vue';
export default {
    components: {
        SignIn
    }
        
    }
        


</script>
<style lang="scss">
.sign-in-page-bg{
    background-image: url('./../assets/Background-log.png');
    height: 100vh;
    .for-show-s-in-be-well{
        opacity: 0; 
    }
}
</style>