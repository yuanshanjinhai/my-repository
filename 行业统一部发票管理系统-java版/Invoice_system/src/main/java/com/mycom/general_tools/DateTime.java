package com.mycom.general_tools;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DateTime {
    public String GetDateTime(){
        DateFormat df = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
        String timeNow = df.format(new Date());
        return timeNow;
    }

    public static void main(String[] args) {
        DateTime ins = new  DateTime();
        String timeNow = ins.GetDateTime();
        System.out.println(timeNow);
    }
}
