import java.util.ArrayList;
import java.util.Random;

public class RandomSuanshi {
    public ArrayList chengfabiao_result(){
        ArrayList chengfabiao_result_list = new ArrayList();
        for(int i0=1;i0<10;i0++){
            for(int i1=1;i1<=i0;i1++){
                chengfabiao_result_list.add(i0*i1);
            }
        }
        return chengfabiao_result_list;
    }

    public static void suanshi(){
        RandomSuanshi inscr = new RandomSuanshi();
        ArrayList cfb_result_list = inscr.chengfabiao_result();

        ArrayList suanshi_list = new ArrayList();
        ArrayList suanshi_result_list = new ArrayList();
        int print_count = 0;
        while (true){
            Random rand = new Random();
            int rand_fuhao = rand.nextInt(4);
            String suanshi = "";
            int result = 0;
            if(rand_fuhao==0 || rand_fuhao==1) {
                while (true){
                    int jiajianshu0 = rand.nextInt(200);
                    int jiajianshu1 = rand.nextInt(200);
                    Integer suanshi_jiashu0 = jiajianshu0;
                    Integer suanshi_jiashu1 = jiajianshu1;
                    if (rand_fuhao == 0) {
                        suanshi = suanshi_jiashu0.toString() + "+" + suanshi_jiashu1.toString() + "=";
                        result = jiajianshu0 + jiajianshu1;
                    }
                    if (rand_fuhao == 1) {
                        suanshi = suanshi_jiashu0.toString() + "-" + suanshi_jiashu1.toString() + "=";
                        result = jiajianshu0 - jiajianshu1;
                    }
                    if (result > 200 || result < 0) {
                        continue;
                    }
                    break;
                }
            }
            if(rand_fuhao==2 || rand_fuhao==3) {
                if (rand_fuhao == 2) {
                    int chengshu0 = rand.nextInt(9);
                    int chengshu1 = rand.nextInt(9);
                    Integer suanshi_chengshu0 = chengshu0;
                    Integer suanshi_chengshu1 = chengshu1;
                    suanshi = suanshi_chengshu0.toString() + "×" + suanshi_chengshu1.toString() + "=";
                    result = chengshu0 * chengshu1;
                }
                if (rand_fuhao == 3) {
                    while (true){
                        int chushu0_index = rand.nextInt(cfb_result_list.size());
                        int chushu0 = (int) cfb_result_list.get(chushu0_index);
                        int chushu1 = rand.nextInt(9);
                        if (chushu1 == 0) {
                            continue;
                        }
                        if(chushu0 % chushu1 != 0){
                            continue;
                        }
                        Integer suanshi_chushu0 = chushu0;
                        Integer suanshi_chushu1 = chushu1;
                        suanshi = suanshi_chushu0.toString() + "÷" + suanshi_chushu1.toString() + "=";
                        result = chushu0 / chushu1;
                        if(result>10){
                            continue;
                        }
                        break;
                    }
                }
            }
            suanshi_list.add(suanshi);
            suanshi_result_list.add(result);
            if(suanshi_list.size()==50){
                for(int isuanshi=0;isuanshi<50;isuanshi++){
                    System.out.print(suanshi_list.get(isuanshi)+"        ");
                    print_count += 1;
                }
                System.out.println();
                System.out.println("------------------------------------------------------------------");
                for (int iresult=0;iresult<50;iresult++){
                    System.out.print(suanshi_list.get(iresult) + suanshi_result_list.get(iresult).toString() + "      ");
                }
                System.out.println();
                System.out.println("------------------------------------------------------------------");
                suanshi_list = new ArrayList();
                suanshi_result_list =new ArrayList();
            }
            if(print_count==1000){
                break;
            }
        }
    }
    public static void main(String[] args) {
        suanshi();
    }
}
