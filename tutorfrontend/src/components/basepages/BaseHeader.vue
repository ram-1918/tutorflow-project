<template>
    <div class="base-header">
        <div class="title">
            <span id="header">TutorFlow <i class="fa fa-cogs"></i></span>
        </div>
        <div class="home">
            <router-link to="/">Home</router-link>
        </div>
    </div>
</template>

<style scoped>
.base-header{
    padding: 12px;
    background-color: #394867;
    /* background-color: rgb(26, 76, 123); */
    margin: 0;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;

}
.title{
    width: 50%;
    text-align: right;
}
.home{
    width: 50%;
    /* background-color: #F6F2D4; */
    text-align: right;
    padding: 8px;
}
a{
    color: #394867;
    background-color: #F6F2D4;
    padding: 8px 16px;
    border-radius: 5px;
}
#header{
    color: #F6F2D4;
    font-family:sans-serif;
    font-size: 1.6rem;
    font-weight:lighter;
    cursor:pointer;
}
</style>