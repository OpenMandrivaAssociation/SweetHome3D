%define		pkgname sweethome3d

%define __noautoreq '.*VERSION.*'

Name:		SweetHome3D 
Version:	3.6
Release:	2
Summary:	Sweet Home 3D is a free interior design application 
License:	GPL
Group:		Graphics
URL:		http://www.sweethome3d.com/
Source0:	%{name}-%{version}-src.zip
#Source0:	%{pkgname}-%{version}.tar.gz
Source1:	FurnitureLibraryEditor-1.7-src.zip
#Source2:	sunflow-0.07.3g-src-diff.zip
Source3:	%{name}-%{version}-javadoc.zip
Patch0:		%{name}.patch
BuildRequires:	ant, java
Requires:	java >= 1.6-sun

%description
Sweet Home 3D is a free interior design application that helps you place your
furniture on a house 2D plan, with a 3D preview.
Available at http://www.sweethome3d.eu/, this program is aimed at people who
want to design their interior quickly, whether they are moving or they just
want to redesign their existing home. Numerous visual guides help you draw the
plan of your home and layout furniture. You may draw the walls of your rooms
upon the image of an existing plan, and then, drag and drop furniture onto the
plan from a catalog organized by categories. Each change in the 2D plan is
simultaneously updated in the 3D view, to show you a realistic rendering of
your layout.

%prep 
%setup -q -n %{name}-%{version}-src
%patch0 -p0

rm -rf lib/windows lib/macosx
%ifarch %{ix86}
rm -rf lib/linux/x64
%else
rm -rf lib/linux/i386
%endif


%build
ant jarExecutable

%install
#mkdir -p %{buildroot}%{_bindir}
#mkdir -p %{buildroot}%{_libdir}
install -Dm0644 install/%{name}-%{version}.jar %{buildroot}%{_datadir}/%{name}/%{name}.jar
mkdir -p %{buildroot}%{_datadir}/%{name}/lib
install -Dm0644 lib/*.jar %{buildroot}%{_datadir}/%{name}/lib
mkdir -p %{buildroot}%{_docdir}/%{name}
install -Dm0644 *.TXT %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_iconsdir}
install -Dm0655 deploy/%{name}*.png %{buildroot}%{_iconsdir}
install -Dm0655 deploy/%{name}*.jpg %{buildroot}%{_iconsdir}
install -Dm0655 deploy/%{name}*.gif %{buildroot}%{_iconsdir}
mkdir -p %{buildroot}%{_bindir}
install -Dm0655 install/linux/%{name} %{buildroot}%{_bindir}/%{name}
%ifarch x86_64 
mkdir -p %{buildroot}%{_libdir}
install -Dm0655 lib/linux/x64/*.so %{buildroot}%{_libdir}/
%else
mkdir -p %{buildroot}%{_libdir}
install -Dm0655 lib/linux/i386/*.so %{buildroot}%{_libdir}/
%endif

# menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Sweet Home 3D
Name[ru]=Милый дом 3D
GenericName=Sweet Home 3D
GenericName[ru]=SweetHome 3D
Comment=Design Application
Comment[ru]=Программа проектирования домашнего интерьера в 3D
Exec=/usr/bin/%{name}
Icon=%{_iconsdir}/%{name}Icon48x48.png
Terminal=false
Type=Application
StartupNotify=true
MimeType=foo/bar;foo2/bar2;
Categories=Application;Graphics;
EOF

#%post
#ln -sf /opt/%{name}/%{name} /usr/bin/sweethome

%postun
rm -rf /usr/bin/sweethome

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/*.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/%{name}.jar
%{_docdir}/%{name}/*.TXT
%{_datadir}/%{name}/lib/*
%{_iconsdir}/*.png
%{_iconsdir}/*.jpg
%{_iconsdir}/*.gif


%changelog
* Wed May 16 2012 Sergey Zhemoitel <serg@mandriva.org> 3.5-4mdv2011.0
+ Revision: 799155
- update to 3.5 release 2
- update to version 3.5
- add new release 3.4
- new version 3.3
- new release 3.3, added package with source code
- add russian comment in .desktop

* Fri Jul 22 2011 Sergey Zhemoitel <serg@mandriva.org> 3.2-1
+ Revision: 690943
- imported package SweetHome3D

