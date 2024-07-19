<template>
    <div class="pagination">
        <span class="material-symbols-outlined previous" v-bind:onclick="previous">arrow_back_ios</span>
        <p>{{ current_page }} / {{ page_number }}</p>
        <span class="material-symbols-outlined next" v-bind:onclick="next">arrow_forward_ios</span>
    </div>
</template>
<script>
export default{
    props: ['previous','next', 'page_number','current_page'],
}
</script>
<style lang="scss" scoped>
div.pagination{
    display: flex;
    background-color: black;
    width: 100px;
    height: 30px;
    color: white;
    justify-content: space-between;
    border-radius: 20px;
    float: right;
    margin-right: 25px;
    
    p{
        font-size: 13px;
        margin-top: 5px;
    }
}

span{
    color: white;
    font-size: 14px;
    margin-top: 8px;
    cursor: pointer;
}
span.previous{
    margin-left: 10px;
}
span.next{
    margin-right: 7px;
}
</style>