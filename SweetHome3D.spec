%define		pkgname sweethome3d

Name:		SweetHome3D 
Version:	3.7
Release:	%mkrel 2
Summary:	Sweet Home 3D is a free interior design application 
License:	GPL
Group:		Graphics
URL:		http://www.sweethome3d.com/
Source0:	%{name}-%{version}-src.zip
#Source0:	%{pkgname}-%{version}.tar.gz
Source1:	FurnitureLibraryEditor-1.9-src.zip
#Source2:	sunflow-0.07.3g-src-diff.zip
Source3:	%{name}-%{version}-javadoc.zip
Patch0:		%{name}.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:	java
BuildRequires:	ant
Requires:	java >= 1.6-sun

%description
Sweet Home 3D is a free interior design application that helps you place your furniture on a house 2D plan, with a 3D preview.
Available at http://www.sweethome3d.eu/, this program is aimed at people who want to design their interior quickly,
whether they are moving or they just want to redesign their existing home. Numerous visual guides help you draw the
plan of your home and layout furniture. You may draw the walls of your rooms upon the image of an existing plan,
and then, drag and drop furniture onto the plan from a catalog organized by categories. Each change in the 2D plan
is simultaneously updated in the 3D view, to show you a realistic rendering of your layout.

%prep 
%setup -q -n %{name}-%{version}-src
#setup1 -q
#setup2 -q
#setup3 -q

#setup -q -n %{name}-%{version}
#patch $RPM_BUILD_DIR/%{name}-%{version}-src/install/linux/%{name} %{PATCH0}

%build
ant jarExecutable

%install
rm -rf $RPM_BUILD_ROOT
#mkdir -p $RPM_BUILD_DIR%{_bindir}
#mkdir -p $RPM_BUILD_DIR%{_libdir}
install -Dm0644 $RPM_BUILD_DIR/%{name}-%{version}-src/install/%{name}-%{version}.jar %{buildroot}%{_datadir}/%{name}/%{name}.jar
mkdir -p %{buildroot}%{_datadir}/%{name}/lib
install -Dm0644 $RPM_BUILD_DIR/%{name}-%{version}-src/lib/*.jar %{buildroot}%{_datadir}/%{name}/lib
mkdir -p %{buildroot}%{_docdir}/%{name}
install -Dm0644 $RPM_BUILD_DIR/%{name}-%{version}-src/*.TXT %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_iconsdir}
install -Dm0655 $RPM_BUILD_DIR/%{name}-%{version}-src/deploy/%{name}*.png %{buildroot}%{_iconsdir}
install -Dm0655 $RPM_BUILD_DIR/%{name}-%{version}-src/deploy/%{name}*.jpg %{buildroot}%{_iconsdir}
install -Dm0655 $RPM_BUILD_DIR/%{name}-%{version}-src/deploy/%{name}*.gif %{buildroot}%{_iconsdir}
mkdir -p %{buildroot}%{_bindir}
#install -Dm0655 $RPM_BUILD_DIR/%{name}-%{version}-src/install/linux/%{name} %{buildroot}%{_bindir}/%{name}
%ifarch x86_64 
mkdir -p %{buildroot}%{_libdir}
install -Dm0655 $RPM_BUILD_DIR/%{name}-%{version}-src/lib/linux/x64/*.so %{buildroot}%{_libdir}/
%else
mkdir -p %{buildroot}%{_libdir}
install -Dm0655 $RPM_BUILD_DIR/%{name}-%{version}-src/lib/linux/i386/*.so %{buildroot}%{_libdir}/
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

# script start program
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh

# Retrieve Sweet Home 3D directory
#PROGRAM=`readlink "$0"`
#if [ "$PROGRAM" = "" ]; then
#  PROGRAM=$0
#  fi
#  PROGRAM_DIR=`dirname "$PROGRAM"`
#  
#  # Run Sweet Home 3D
#  exec "$PROGRAM_DIR"/jre1.6.0_37/bin/java -Xmx1024m -classpath "$PROGRAM_DIR"/lib/SweetHome3D.jar:"$PROGRAM_DIR"/lib/Furniture.jar:"$PROGRAM_DIR"//lib/Textures.jar:"$PROGRAM_DIR"/lib/Help.jar:"$PROGRAM_DIR"/lib/Loader3DS1_2u.jar:"$PROGRAM_DIR"/lib/iText-2.1.7.jar:"$PROGRAM_DIR"/lib/freehep-vectorgraphics-svg-2.1.1.jar:"$PROGRAM_DIR"/lib/sunflow-0.07.3g.jar:"$PROGRAM_DIR"/lib/jmf.jar:"$PROGRAM_DIR"/lib/batik-svgpathparser-1.7.jar:"$PROGRAM_DIR"/lib/j3dcore.jar:"$PROGRAM_DIR"/lib/j3dutils.jar:"$PROGRAM_DIR"/lib/vecmath.jar:"$PROGRAM_DIR"/jre1.6.0_37/lib/javaws.jar -Djava.library.path="$PROGRAM_DIR"/lib com.eteks.sweethome3d.SweetHome3D -open "$1"

exec java -jar /usr/share/SweetHome3D/SweetHome3D.jar

EOF

chmod +x %{buildroot}%{_bindir}/%{name}

%clean

rm -rf $RPM_BUILD_ROOT

#%post
#ln -sf /opt/%{name}/%{name} /usr/bin/sweethome

%postun
rm -rf /usr/bin/%{name}

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
