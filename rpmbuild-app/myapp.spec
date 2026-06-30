Name:           myapp
Version:        %{app_version}
Release:        %{app_release}%{?dist}
Summary:        My First Custom RPM Package
License:        MIT
BuildArch:      noarch

%description
A simple custom application packaged as RPM,
built and deployed via Jenkins + Ansible pipeline.

%install
mkdir -p %{buildroot}/usr/local/bin
cp %{_sourcedir}/usr/local/bin/myapp.sh %{buildroot}/usr/local/bin/myapp.sh

%files
/usr/local/bin/myapp.sh

%post
chmod +x /usr/local/bin/myapp.sh

%changelog
* Mon Jun 30 2026 Rahul Vanmali <rahul@example.com> - %{app_version}-%{app_release}
- Build %{app_version}
