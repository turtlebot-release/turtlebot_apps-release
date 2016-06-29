Name:           ros-kinetic-turtlebot-actions
Version:        2.3.5
Release:        0%{?dist}
Summary:        ROS turtlebot_actions package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/turtlebot_actions
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-actionlib-msgs
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-image-geometry
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-turtlebot-bringup
BuildRequires:  eigen3-devel
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-actionlib-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-image-geometry
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-tf

%description
turtlebot_actions provides several basic actionlib actions for the TurtleBot.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Jun 28 2016 OSRF <turtlebot@osrfoundation.org> - 2.3.5-0
- Autogenerated by Bloom

