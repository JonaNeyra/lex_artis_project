## URLs

```python
NOM_URLS = {
    "NOM_016_SSA3_2012": "https://www.dof.gob.mx/nota_detalle.php?codigo=5284306&fecha=08/01/2013#gsc.tab=0",
    "NOM_026_SSA3_2012": "https://www.dof.gob.mx/nota_detalle.php?codigo=5262609&fecha=07/08/2012#gsc.tab=0",
    "NOM_004_SSA3_2012": "https://dof.gob.mx/nota_detalle.php?codigo=5272787&fecha=15/10/2012#gsc.tab=0",
}
```

## gRPC Generation

### Example:

```bash
python -m grpc_tools.protoc -I=medical_act/src/resources/protos --python_out=medical_act/src/resources/protos --pyi_out=medical_act/src/resources/protos --grpc_python_out=medical_act/src/resources/protos medical_act/src/resources/protos/extractnomfromurlpb/extractnomfromurlpb.proto
```