<template>
    <div :class="type">
        <span class="title">
            <slot>{{ title }}</slot>
        </span>
    </div>
</template>

<script>
export default {
    props: ['type', 'title']
};
</script>

<style scoped>
div{
    border: none;
    padding: 20px;
    width: fit-content;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    aspect-ratio: 16/6;

}
.nothing{
    /* background-color: rgb(225, 229, 232); */
}
.title{
    font-size: larger;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    font-size: bolder;
}
.page-not-found{
    margin: auto;
    font-weight: bold;
    font-size: larger;
    position: fixed;
    top:10%;
    left: 36%;
}

</style>