package io.dataspaceconnector.common.net;

import lombok.Data;
import org.springframework.web.multipart.MultipartFile;

import java.util.ArrayList;
import java.util.List;

@Data
public class PayloadWrapper {

    private List<MultipartFile> files = new ArrayList<>();

    private String payload = "";

    public void setPayload(Object payload){
        this.payload = String.valueOf(payload);
    }
}


