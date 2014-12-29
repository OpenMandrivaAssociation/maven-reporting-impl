%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-reporting-impl
Version:        2.3
Release:        1.1
Summary:        Abstract classes to manage report generation
Group:		Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/shared/%{name}
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/reporting/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Forwarded upstream: http://jira.codehaus.org/browse/MSHARED-344
Patch0:         0001-Update-to-Doxia-1.6.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-validator:commons-validator)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
%{?fedora:BuildRequires: junit-addons}

Obsoletes:      maven-shared-reporting-impl < %{version}-%{release}
Provides:       maven-shared-reporting-impl = %{version}-%{release}

%description
Abstract classes to manage report generation, which can be run both:

* as part of a site generation (as a maven-reporting-api's MavenReport),
* or as a direct standalone invocation (as a maven-plugin-api's Mojo).

This is a replacement package for maven-shared-reporting-impl

%package javadoc
Summary:        Javadoc for %{name}
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

%build
%mvn_build %{!?fedora:-f}

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Sep 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-1
- Update to upstream version 2.3

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-11
- Fix build-requires on parent POM
- Port to Doxia 1.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-9
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-8
- Fix unowned directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-6
- Add missing BuildRequires

* Mon Apr  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-5
- Skip running tests outsides Fedora

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-4
- Build with xmvn

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Feb 05 2013 Michal Srb <msrb@redhat.com> - 2.2-2
- Migrate from maven-doxia to doxia subpackages

* Fri Jan 11 2013 Tomas Radej <tradej@redhat.com> - 2.2-1
- Initial version

