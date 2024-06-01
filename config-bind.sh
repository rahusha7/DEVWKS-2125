echo "packages:
- name: "bind"
  release: "ThinXR_7.3.15"
  version: "1.0.1"
  sources:
    - name: bind
      file: bind9/bind.tar.gz
  config-dir:
    - name: bind-configs
      dir: bind9/config" > ~/xr-appmgr-build/bind9/build.yaml