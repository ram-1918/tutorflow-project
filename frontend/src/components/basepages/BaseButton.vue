<template>
    <button v-if="!link" :type = "type" :class="mode">
      <slot></slot>
    </button>
    <router-link v-else :to="to" :class="mode">
      <slot></slot>
    </router-link>
  </template>

<script>
export default {
    props: ['type', 'mode', 'link', 'to']
};
</script>

<style scoped>
.private-mode{
    /* background-color: #03A9F4; */
    background-color:inherit;
    border: none;
    outline: none;
    color: red;
    padding: 12px 20px;
    width: 110px;
    border-top-right-radius: 10rem;
    border-top-left-radius: 10rem;
    border-bottom-right-radius: 10rem;
    border-bottom-left-radius: 10rem;
    transition: 0.3s cubic-bezier(0.18, 0.89, 0.35, 1.15) all;
}
.public-mode{
    /* background-color: #03A9F4; */
    background-color: inherit;
    border: none;
    outline: none;
    color: black;
    padding: 12px 20px;
    width: 110px;
    border-top-right-radius: 10rem;
    border-top-left-radius: 10rem;
    border-bottom-right-radius: 10rem;
    border-bottom-left-radius: 10rem;
    transition: 0.3s cubic-bezier(0.18, 0.89, 0.35, 1.15) all;
}

.tag{
    background-color: rgb(209, 226, 243);
    color: black;
    border-radius: 5px;
    border: none;
    padding: 7px;
    margin: 0.5rem;
    font-size: small;
    cursor: pointer;
    box-shadow: 1px 3px 4px rgba(0,0,0,0.4);
}
.search-tag{
    background-color: rgb(199, 219, 238);
    color: black;
    border-radius: 5px;
    border: none;
    padding: 5px;
    margin: 0.1rem;
    font-size: small;
    cursor: pointer;
    box-shadow: 1px 3px 4px rgba(0,0,0,0.4);
}
.add{
    /* background-color: red; */
    /* color: rgb(24, 57, 124); */
    outline: none;
    border: none;
    padding: 12px 18px;
    margin-right: 0.5rem;
    cursor:pointer;
    font-weight:900;
    float: right;
}
.add:hover{
    opacity: 0.8;
}
.delete{
    background-color: inherit; /* dark mode */
    color: black; /* dark mode */
    border: none;
    cursor: pointer;
}
.submit{
    background-color: rgb(43, 88, 130);
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 100%;
}
.submit:hover{
    opacity: 0.8;
}
.feedback-submit{
    width:fit-content;
    border: none;
    background-color: rgb(19, 78, 161);
    border-radius: 5px;
    padding:5px 13px;
    margin: 0.5rem;
    color: white;
    font-weight: 100;
    font-size: small;
    outline: none;
    cursor: pointer;
}
.session-button{
    border: none;
    background-color: inherit;
    padding: 13px 10px;
    color: #D1D2D3;
    font-weight: 100;
    outline: none;
    cursor: pointer;
}
.topnavButton{
    background-color: inherit;
    color: white;
    padding: 13px 15px;
    border: none;
    outline: none;
    cursor: pointer;
}
.post{
    border: none;
    background-color: rgb(23, 93, 159) ;
    color: white;
    padding: 12px 18px;
    width: 150px;
    border-radius: 10px;
    cursor: pointer;
    margin: 0.5rem;
}
.text-style{
    background: inherit;
    border: none;
    cursor: pointer;
}

.delete:hover{
    color: red;
}

.topnavButton:hover{
    background-color: rgb(63, 118, 169);
}
.post:hover{
    opacity: 0.85;
}
.active{
    background-color: rgb(63, 118, 169);
}
.text-style:hover{
    opacity: 0.85;
}

</style>