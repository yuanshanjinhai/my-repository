package com.mycom.service.impl.alllist;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.mycom.mapper.SystemDepartmentListByCompanyMapper;
import com.mycom.model.SystemDepartmentListByCompanyVO;
import com.mycom.service.alllist.ListDepartmentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@Service
public class ListDepartmentImpl extends ServiceImpl<SystemDepartmentListByCompanyMapper, SystemDepartmentListByCompanyVO> implements ListDepartmentService {
    @Autowired
    SystemDepartmentListByCompanyMapper systemCompanyDepartmentMapper;

    @Override
    public LinkedHashMap GeDepartmentList(Integer companyId){
        ArrayList<Map> rlist0 = systemCompanyDepartmentMapper.selectDepartmentList(companyId);
        System.out.println("rlist0=" +rlist0);
        List rlist = new ArrayList();

        if (rlist != null){
            for(int i =0;i<rlist0.size();i++){
                Map lmp0 = new LinkedHashMap();
                lmp0.put("id",rlist0.get(i).get("id"));
                lmp0.put("user_name",rlist0.get(i).get("department_name"));
                rlist.add(lmp0);
            }
        }
        Map lmp = new LinkedHashMap();
        lmp.put("code",1);
        lmp.put("info","success");
        lmp.put("data",rlist);
        return (LinkedHashMap) lmp;
    }
}
