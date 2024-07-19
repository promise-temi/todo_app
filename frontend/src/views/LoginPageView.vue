<template>
    <div class="log-in-page-bg">
        <span class="for-show-l-in-be-well">hello</span>
        <LogIn></LogIn>
    </div>
</template>
<script>
import LogIn from '@/components/LogIn.vue';
export default {
    components: {
        LogIn
    }
}
</script>
<style lang="scss" >
.log-in-page-bg{
    background-image: url('./../assets/Background-log.png');
    height: 100vh;
    .for-show-l-in-be-well{
        opacity: 0; 
    }
}
</style>