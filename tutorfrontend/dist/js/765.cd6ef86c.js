"use strict";(self["webpackChunktutorfrontend"]=self["webpackChunktutorfrontend"]||[]).push([[765],{5765:function(e,t,s){s.r(t),s.d(t,{default:function(){return x}});var i=s(3396),r=s(9242),n=s(7139);const l=e=>((0,i.dD)("data-v-35ab6148"),e=e(),(0,i.Cn)(),e),o={id:"id01",class:"modal"},a={key:0,class:"error-msg"},d=l((()=>(0,i._)("br",null,null,-1))),u={key:1,class:"error-msg"},m=l((()=>(0,i._)("br",null,null,-1))),p=l((()=>(0,i._)("span",{class:"login-title"},"Login",-1))),_=l((()=>(0,i._)("br",null,null,-1))),h={class:"container"},w=l((()=>(0,i._)("legend",null,"Email",-1))),c={key:0,class:"error-msg"},f=l((()=>(0,i._)("br",null,null,-1))),k=l((()=>(0,i._)("span",{class:"login-title"},"Login",-1))),g=l((()=>(0,i._)("br",null,null,-1))),v={class:"container"},y=l((()=>(0,i._)("legend",null,"Email",-1))),b=l((()=>(0,i._)("legend",null,"OTP",-1))),U={key:0,class:"error-msg"},S=l((()=>(0,i._)("br",null,null,-1))),$=l((()=>(0,i._)("span",{class:"login-title"},"Reset password",-1))),q=l((()=>(0,i._)("br",null,null,-1))),D={class:"container"},I=l((()=>(0,i._)("legend",null,"password",-1))),T=l((()=>(0,i._)("legend",null,"Re-enter password",-1)));function V(e,t,s,l,V,W){const P=(0,i.up)("base-header"),R=(0,i.up)("base-button"),L=(0,i.up)("router-link");return(0,i.wg)(),(0,i.iD)(i.HY,null,[(0,i.Wm)(P),(0,i._)("div",o,[V.token_sent||V.is_verified?V.token_sent&&!V.is_verified?((0,i.wg)(),(0,i.iD)("form",{key:1,class:"modal-content",onSubmit:t[4]||(t[4]=(0,r.iM)((e=>W.verifyToken()),["prevent"]))},[this.$store.state.err?((0,i.wg)(),(0,i.iD)("span",c,(0,n.zw)(this.$store.state.err),1)):(0,i.kq)("",!0),f,k,g,(0,i._)("div",v,[(0,i._)("fieldset",null,[y,(0,i.wy)((0,i._)("input",{type:"text",placeholder:"","onUpdate:modelValue":t[2]||(t[2]=e=>V.email=e),disabled:""},null,512),[[r.nr,V.email]])]),(0,i._)("fieldset",null,[b,(0,i.wy)((0,i._)("input",{type:"text",placeholder:"","onUpdate:modelValue":t[3]||(t[3]=e=>V.token=e),required:""},null,512),[[r.nr,V.token]])]),(0,i.Wm)(R,{type:"submit",mode:"submit"},{default:(0,i.w5)((()=>[(0,i.Uk)("Verify")])),_:1}),(0,i.Uk)(" or SignIn using "),(0,i.Wm)(L,{to:"/login"},{default:(0,i.w5)((()=>[(0,i.Uk)("SignIn")])),_:1})])],32)):((0,i.wg)(),(0,i.iD)("form",{key:2,class:"modal-content",onSubmit:t[7]||(t[7]=(0,r.iM)((e=>W.resetPassword()),["prevent"]))},[this.$store.state.err?((0,i.wg)(),(0,i.iD)("span",U,(0,n.zw)(this.$store.state.err),1)):(0,i.kq)("",!0),S,$,q,(0,i._)("div",D,[(0,i._)("fieldset",null,[I,(0,i.wy)((0,i._)("input",{type:"password",placeholder:"","onUpdate:modelValue":t[5]||(t[5]=e=>V.password=e),required:""},null,512),[[r.nr,V.password]])]),(0,i._)("fieldset",null,[T,(0,i.wy)((0,i._)("input",{type:"password",placeholder:"","onUpdate:modelValue":t[6]||(t[6]=e=>V.cnfpassword=e),required:""},null,512),[[r.nr,V.cnfpassword]])]),(0,i.Wm)(R,{type:"submit",mode:"submit"},{default:(0,i.w5)((()=>[(0,i.Uk)("Reset")])),_:1}),(0,i.Uk)(" or SignIn using "),(0,i.Wm)(L,{to:"/login"},{default:(0,i.w5)((()=>[(0,i.Uk)("SignIn")])),_:1})])],32)):((0,i.wg)(),(0,i.iD)("form",{key:0,class:"modal-content",onSubmit:t[1]||(t[1]=(0,r.iM)((e=>W.sendToken()),["prevent"]))},[this.$store.state.err?((0,i.wg)(),(0,i.iD)("span",a,(0,n.zw)(this.$store.state.err),1)):(0,i.kq)("",!0),d,this.error?((0,i.wg)(),(0,i.iD)("span",u,(0,n.zw)(this.error),1)):(0,i.kq)("",!0),m,p,_,(0,i._)("div",h,[(0,i._)("fieldset",null,[w,(0,i.wy)((0,i._)("input",{type:"text",placeholder:"","onUpdate:modelValue":t[0]||(t[0]=e=>V.email=e),required:""},null,512),[[r.nr,V.email,void 0,{trim:!0}]])]),(0,i.Wm)(R,{type:"submit",mode:"submit"},{default:(0,i.w5)((()=>[(0,i.Uk)("Request token")])),_:1}),(0,i.Uk)(" or SignIn using "),(0,i.Wm)(L,{to:"/login"},{default:(0,i.w5)((()=>[(0,i.Uk)("SignIn")])),_:1})])],32))])],64)}var W=s(4161),P={data(){return{id:"",email:"",token:"",password:"",cnfpassword:"",text:"",is_verified:!1,token_sent:!1,error:""}},methods:{sendToken(){this.error="";var e=/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/;if(this.email=this.email.trim().toLowerCase(),e.test(this.email)){var t={email:this.email};W.Z.post(this.$store.state.API_URL1+"forgot-password/",t).then((e=>{console.log(e.data),this.id=e.data["id"],this.token_sent=e.data["token_sent"],this.error=this.token_sent?"":"This email is not registered!"})).catch((()=>{alert("gre"),this.error="Enter valid email address!"}))}else this.error="Enter valid email address!"},verifyToken(){var e={email:this.email,token:this.token};W.Z.post(this.$store.state.API_URL1+"verify-fp/",e).then((e=>{console.log(e.data),this.is_verified=e.data["verified"],this.token_sent=!1,this.is_verified_msg="Verified Sucessfully!",setTimeout((()=>{this.is_verified_msg=""}),5500)})).catch((()=>{this.token_sent=!0}))},resetPassword(){if(this.password===this.cnfpassword){const e={id:this.id,email:this.email,password:this.password};this.$store.dispatch("resetpassword",e)}else this.error="Passwords did not match!"}}},R=s(89);const L=(0,R.Z)(P,[["render",V],["__scopeId","data-v-35ab6148"]]);var x=L}}]);
//# sourceMappingURL=765.cd6ef86c.js.map