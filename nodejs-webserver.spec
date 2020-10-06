Name:           nodejs-webserver-1
Version:        1.4.2
Release:        1%{?dist}
Summary:        Small Node.js web server
License:        MIT License
URL:            https://nodejs.org
Source0:        nodejs-webserver-1-1.4.2.tgz

%description
This package provides the web server and is part of a larger software solution

%prep
%setup -n package

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin/small_nodejs_server
chmod 755 index.js
cp -ar ./* $RPM_BUILD_ROOT/usr/bin/small_nodejs_server/

%files
/usr/bin/small_nodejs_server/index.js
/usr/bin/small_nodejs_server/package.json
%doc /usr/bin/small_nodejs_server/README.md
%config /usr/bin/small_nodejs_server/configs/dev_conf.json
/usr/bin/small_nodejs_server/configs/example_conf.json

%changelog