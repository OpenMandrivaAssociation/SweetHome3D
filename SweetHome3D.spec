%define         pkgname         sweethome3d
%define         pkgmod          3DModels
%define         modelver        1.3.2
%define         debug_package   %{nil}

%define __noautoreq '.*VERSION.*'

Name:		SweetHome3D
Version:	4.4
Release:	1
Summary:	Sweet Home 3D is a free interior design application 
License:	GPLv2+
Group:		Graphics
URL:		http://www.sweethome3d.com/
Source0:        %{name}-%{version}-src.zip
#Source1:        FurnitureLibraryEditor-1.12-src.zip
#Source2:      sunflow-0.07.3g-src-diff.zip
Source3:        %{name}-%{version}-javadoc.zip
#Source4:        %{pkgmod}-Contributions-%{modelver}.zip
#Source5:        %{pkgmod}-KatorLegaz-%{modelver}.zip
#Source6:        %{pkgmod}-LucaPresidente-%{modelver}.zip
#Source7:        %{pkgmod}-Reallusion-%{modelver}.zip
#Source8:        %{pkgmod}-Scopia-%{modelver}.zip
#Source9:        %{pkgmod}-Trees-%{modelver}.zip
#Source10:       %{pkgmod}-BlendSwap-CC-0-%{modelver}.zip
#Source11:       %{pkgmod}-BlendSwap-CC-BY-%{modelver}.zip
#Source12:       TexturesLibraryEditor-1.3-src.zip
#Patch0:               %{name}.patch
BuildRequires:  java
BuildRequires:  ant
Requires:       java >= 1.6-sun
Requires:       java3d

%description
Sweet Home 3D is a free interior design application
that helps you place your furniture on a house 2D
plan, with a 3D preview.
Available at http://www.sweethome3d.eu/, this program
is aimed at people who want to design their interior
quickly, whether they are moving or they just want
to redesign their existing home. Numerous visual
guides help you draw the plan of your home and
layout furniture. You may draw the walls of your
rooms upon the image of an existing plan, and then,
drag and drop furniture onto the plan from a catalog
organized by categories. Each change in the 2D plan
is simultaneously updated in the 3D view, to show
you a realistic rendering of your layout.

%prep 
%setup -q -n %{name}-%{version}-src

#rm -rf lib/windows lib/macosx
%ifarch %{ix86}
rm -rf lib/linux/x64
%else
rm -rf lib/linux/i386
%endif


%build
ant jarExecutable

%install
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
%if %mdkversion  <= 201200
%ifarch x86_64
mkdir -p %{buildroot}%{_libdir}
install -Dm0655 lib/linux/x64/*.so %{buildroot}%{_libdir}/
%else
mkdir -p %{buildroot}%{_libdir}
install -Dm0655 lib/linux/i386/*.so %{buildroot}%{_libdir}/
%endif
%endif

# menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Sweet Home 3D
Name[ru]=Sweet Home 3D
GenericName=Sweet Home 3D
GenericName[ru]=SweetHome 3D
Comment=Design Application
Comment[ru]=Проектирования домашнего интерьера в 3D
Exec=/usr/bin/%{name}
Icon=%{_iconsdir}/%{name}Icon48x48.png
Terminal=false
Type=Application
StartupNotify=true
MimeType=application/octet-stream;application/SweetHome3D;
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

exec java -Xmx1024m -jar /usr/share/SweetHome3D/SweetHome3D.jar

EOF

chmod +x %{buildroot}%{_bindir}/%{name}


%files
%defattr(-,root,root)
%{_bindir}/%{name}
%if %mdkversion <= 201200
%{_libdir}/*.so
%endif
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/%{name}.jar
%{_docdir}/%{name}/*.TXT
%{_datadir}/%{name}/lib/*
%{_iconsdir}/*.png
%{_iconsdir}/*.jpg
%{_iconsdir}/*.gif
