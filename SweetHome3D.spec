Name:		SweetHome3D 
Version:	3.3
Release:	%mkrel 1
Summary:	Sweet Home 3D is a free interior design application 
License:	GPL
Group:		Graphics

URL:		http://www.sweethome3d.com/
#Source0:	sweethome_3d-2.6.tar.bz2
Source0:	sweethome3d-%{version}.tar.gz
Patch0:		sweethome.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

Requires:	java >= 1.6-sun

%description

Sweet Home 3D is a free interior design application that helps you place your furniture on a house 2D plan, with a 3D preview.

Available at http://www.sweethome3d.eu/, this program is aimed at people who want to design their interior quickly, whether they are moving or they just want to redesign their existing home. Numerous visual guides help you draw the plan of your home and layout furniture. You may draw the walls of your rooms upon the image of an existing plan, and then, drag and drop furniture onto the plan from a catalog organized by categories. Each change in the 2D plan is simultaneously updated in the 3D view, to show you a realistic rendering of your layout.

%prep 
%setup -q -n %{name}
#%setup -q -n %{name}-%{version}
#%__patch -p1 %{name} %{PATCH0}

%build
ant

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/opt/%{name}
mkdir -p %{buildroot}/opt/%{name}/lib
install -Dm0644 $RPM_BUILD_DIR/%{name}-%{version}/*.TXT %{buildroot}/opt/%{name}
install -Dm0655 $RPM_BUILD_DIR/%{name}-%{version}/%{name} %{buildroot}/opt/%{name}/%{name}
install -Dm0644 $RPM_BUILD_DIR/%{name}-%{version}/lib/* %{buildroot}/opt/%{name}/lib

# menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Sweet Home 3D
Name[ru]=Милый дом 3D
GenericName=Sweet Home 3D
GenericName[ru]=Милый дом 3D
Comment=Design Application
Comment[ru]=Программа проектирования домашнего интерьера в 3D
Exec=/usr/bin/sweethome
Icon=/usr/lib/sweethome_3d/sweethome.png
Terminal=false
Type=Application
StartupNotify=true
MimeType=foo/bar;foo2/bar2;
Categories=Application;Graphics;
EOF

%clean

rm -rf $RPM_BUILD_ROOT

%post
ln -sf /opt/%{name}/%{name} /usr/bin/sweethome

%postun
rm -rf /usr/bin/sweethome

%files
%defattr(-,root,root)
%{_datadir}/applications/%{name}.desktop
/opt/%{name}/%{name}
/opt/%{name}/*.TXT
/opt/%{name}/lib/*

#/usr/*
#/usr/lib/*
#/usr/share/*

