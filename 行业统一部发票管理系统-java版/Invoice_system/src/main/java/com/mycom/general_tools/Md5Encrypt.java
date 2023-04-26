package com.mycom.general_tools;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Md5Encrypt {
    public String getmd5(String pwd) {
        String hashedPwd = null;
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");// 生成一个MD5加密计算摘要
            md.update(pwd.getBytes());// 计算md5函数
            /**
             * digest()最后确定返回md5 hash值，返回值为8位字符串。
             * 因为md5 hash值是16位的hex值，实际上就是8位的字符
             * BigInteger函数则将8位的字符串转换成16位hex值，用字符串来表示；得到字符串形式的hash值
             * 一个byte是八位二进制，也就是2位十六进制字符（2的8次方等于16的2次方）
             */
            hashedPwd = new BigInteger(1, md.digest()).toString(16);

        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return hashedPwd;
    }
    public static void main(String[] args) {
        Md5Encrypt ins = new Md5Encrypt();
        String md5Password = ins.getmd5("123456");
        System.out.println("md5Password=" +md5Password);
    }
}
