const crypto = require('crypto');

function encrypt(text, key) {
  const cipher = crypto.createCipheriv('aes-128-ecb', key, Buffer.from('')); // 使用aes-128-ecb加密方式，传入空的iv
  let encrypted = cipher.update(text, 'utf8', 'base64');
  encrypted += cipher.final('base64');
  return encrypted;
}

// 要加密的文本和密钥
const text = '15878265826!';
const key = 'czg3UGZEM0ZjekU1ejAxWGFCNllhY2JHOWxRYzIwQTM=';

// 输出加密后的文本
console.log(encrypt(text, key));