<template>
    <div class="date"><img src="../assets/Calendar.png" alt=""><p id="curent-date"></p></div>
</template>
<script>

export default{
    methods:{
        date(){
            let date1 = new Date();

let dateperso = date1.toLocaleString('fr-FR',{
    weekday: 'long',
    day: 'numeric',
    month: 'short',
    year: 'numeric',
    });

document.getElementById('curent-date').innerHTML = dateperso;
        }
    },
    mounted(){
        this.date();
    }
}

</script>
<style lang="scss" scoped>
div.date{
    padding-top: 40px;
    margin-left: 35px;
    display: flex;
    
}
img{
    width: 20px;
    height: 20px;
    margin-top: 3px;
    margin-right: 10px;
}
p{
    color: #15192C !important;
    font-size: 18px;
    font-weight: 400;
    white-space: nowrap;
}
p::first-letter {
    text-transform:capitalize;
}
</style>