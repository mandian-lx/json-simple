%define commit a8b94b79b697df64b23428c27d65d6a187e9ebf9
%define shortcommit %(c=%{commit}; echo ${c:0:7})

%define ver %(echo %version | tr \. _)

Summary:	Java implementation of D-Bus
Name:		json-simple
Version:	1.1.1
Release:	1
License:	Apache License
Group:		Development/Java
URL:		https://github.com/fangyidong/%{name}/
#Source0:	https://github.com/fangyidong/%{name}/archive/tag_release_%{ver}.tar.gz
Source0:	https://github.com/fangyidong/%{name}/archive/%{commit}/%{name}-%{commit}.zip
BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-source-plugin)

Requires:	java-headless
Requires:	javapackages-tools

%description
json-simple is a simple Java implementation of D-Bus.

%files -f .mfiles
%doc README.txt
%doc ChangeLog.txt
%doc LICENSE.txt
%doc AUTHORS.txt
%doc VERSION.txt

#----------------------------------------------------------------------------

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%files javadoc -f .mfiles-javadoc

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{commit}
find . -type f -name "*.jar" -delete
find . -type f -name "*.class" -delete

# Fix JAR name
%mvn_file :%{name} %{name}-%{version} %{name}

%build
%mvn_build

%install
%mvn_install

