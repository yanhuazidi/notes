
const mysql = require('mysql');
var connection = mysql.createPool({    //创建连接
    host:'192.168.0.15',
    port:'3306',
    user:'wei',
    password:'123456',
    database:'xz',
    connectionLimit:20
});

connection.query('select * from ',(err,result)=>{
    // if(err) throw err;
    console.log(result);
});  //执行sql语句

connection.query('select * from ',(err,result)=>{
    // if(err) throw err;
    console.log(result);
});  //执行sql语句


